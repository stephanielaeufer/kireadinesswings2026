"""Prüft konkrete Fehlerfolgen mit ausschließlich synthetischen Antworten."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('score', ROOT/'auswertung/score.py')
score = importlib.util.module_from_spec(spec); spec.loader.exec_module(score)

class ScoringChecks(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT/'beispiele/synthetische_antworten.json').read_text(encoding='utf-8'))

    def test_zero_remains_valid_and_missing_is_not_imputed(self):
        out = score.evaluate(self.data)
        self.assertEqual(out['items']['U01']['n_valid'], 2)
        self.assertEqual(out['items']['U01']['distribution']['0']['n'], 2)
        self.assertEqual(out['items']['U01']['missing_by_reason']['NICHT_BEURTEILBAR'], 1)
        self.assertIsNone(out['individual_scores'][1]['scores']['U'])
        self.assertEqual(out['domains']['U']['mean'], 1.25)
        self.assertEqual(out['domains']['U']['n_complete'], 2)
        self.assertIsNone(out['total_score'])
        self.assertNotIn('G', out['domains'])

    def test_multi_answer_denominator_counts_people(self):
        out = score.evaluate(self.data)['items']['W01']
        self.assertEqual(out['n_valid'], 3)
        self.assertAlmostEqual(out['distribution']['BASICS']['percent_valid'], 100/3)

    def test_empty_data_have_no_fabricated_zero_mean(self):
        self.data['records'] = []
        out = score.evaluate(self.data)
        self.assertIsNone(out['domains']['U']['mean'])
        self.assertIsNone(out['items']['U01']['distribution']['0']['percent_valid'])

    def test_completely_missing_answers_have_no_person_scores(self):
        self.data['records'] = self.data['records'][:1]
        for a in self.data['records'][0]['answers'].values():
            a.update(value=None, missing_reason='KEINE_ANGABE')
        out=score.evaluate(self.data)
        self.assertTrue(all(s is None for s in out['individual_scores'][0]['scores'].values()))
        self.assertEqual(out['items']['U01']['n_valid'],0)

    def test_invalid_capture_is_missing_not_imputed(self):
        # Codebuch-Revision 0.6: ungültig erfasster Wert bleibt fehlend und getrennt gezählt.
        self.data['records'][0]['answers']['U03'] = {'value': None, 'missing_reason': 'UNGUELTIG_ERFASST'}
        out = score.evaluate(self.data)
        self.assertEqual(out['items']['U03']['missing_by_reason']['UNGUELTIG_ERFASST'], 1)
        self.assertEqual(out['items']['U03']['missing_by_reason']['KEINE_ANGABE'], 0)
        self.assertIsNone(out['individual_scores'][0]['scores']['U'])
        self.assertEqual(out['domains']['U']['n_complete'], 1)
        self.assertEqual(out['items']['C01']['missing_by_reason']['UNGUELTIG_ERFASST'], 0)

    def test_invalid_inputs_are_rejected(self):
        mutations = [
            lambda d: d.update(data_kind='DEMO'),
            lambda d: d.update(questionnaire_version='GARI-DE-9'),
            lambda d: d['records'][0].update(questionnaire_version='GARI-DE-0.2'),
            lambda d: d['records'].append(copy.deepcopy(d['records'][0])),
            lambda d: d['records'][0]['answers'].pop('G01'),
            lambda d: d['records'][0]['answers'].update(FAKE={'value':1,'missing_reason':None}),
            lambda d: d['records'][0]['answers']['U01'].update(value=11),
            lambda d: d['records'][0]['answers']['U01'].update(value=True),
            lambda d: d['records'][0]['answers']['A01'].update(value=0),
            lambda d: d['records'][0]['answers']['U01'].update(value=0,missing_reason='NICHT_BEURTEILBAR'),
            lambda d: d['records'][0]['answers']['U01'].update(value=None,missing_reason=None),
            lambda d: d['records'][0]['answers']['U01'].update(value=None,missing_reason='NICHT_ZUTREFFEND'),
            lambda d: d['records'][0]['answers']['W01'].update(value=['NONE','BASICS']),
            lambda d: d['records'][0]['answers']['W01'].update(value=[]),
            lambda d: d['records'][0]['answers']['W01'].update(value=['BASICS']*2),
            lambda d: d['records'][0]['answers']['W01'].update(value=['BASICS','PROMPTING','VERIFY','DATA_RULES']),
        ]
        for n, mutate in enumerate(mutations):
            with self.subTest(case=n):
                data=copy.deepcopy(self.data); mutate(data)
                with self.assertRaises(ValueError): score.evaluate(data)

if __name__=='__main__': unittest.main()
