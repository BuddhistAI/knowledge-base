---
id: tuvan
title: Tuvan
kind: modern
group: Mongolic and Turkic
countries: [Russia, China]
scripts: [Cyrillic]
speakers: about 253,000 native speakers (2020; Rosstat via Wikipedia [1])
speakers_n: 252953
speakers_year: 2020
speakers_source: https://en.wikipedia.org/wiki/Tuvan_language
speakers_basis: first-language speakers
directory_names: [Tuvan]
resource_level: very low
google_translate: yes (since 2024)
recommendation: Google Translate or Yandex compared with a frontier LLM on a small test
confidence: low
updated: 2026-11
contributors: []
---

# Tuvan

Tuvan is a Turkic language of the Republic of Tuva in Russia, with a small group of speakers in China. It is not a Mongolic language, but it is grouped here with its Buddhist neighbours. Google and Yandex translate into Tuvan, but there is no public test of their quality. Russian is the common working language.

## Summary

| | |
| --- | --- |
| Where | Republic of Tuva, Russia; Jungar Tuvan speakers in China (counted as Mongols) [1] |
| Speakers | 252,953 native speakers (2020, Rosstat) [1] |
| Script | Cyrillic with Ң, Ө, Ү [1] |
| AI resources | very low |
| Google Translate | yes, added 27 June 2024 [2][3]; not on the Google Cloud language page [4] |
| Microsoft Translator | no [5] |
| Speech to text | not in Whisper [6] or Omnilingual ASR [7] |
| Best evidence on translation quality | none found; a FLORES test set for Tuvan exists (2024) [8] |

## Writing and text input

Tuvan uses Cyrillic with three extra letters (Ң, Ө, Ү) [1]. Standard Cyrillic tools should work, but check that OCR and keyboards handle these letters. We did not test this.

Activists say Russian census language data overstate real language use [9].

## Data

- **Tuvan–Russian parallel 50k** (Agisight): 50,000 sentence pairs sampled from the tyvan.ru Russian–Tuvan corpus; CC BY-SA 4.0 [10].
- **FLORES for Tuvan** (WMT 2024 OLDI shared task): native speakers translated the FLORES sentences from Russian into Tuvan [8]. Size and data license are not stated on the abstract page.

We found no Buddhist text in Tuvan as a dataset.

## Speech

Whisper has no Tuvan code [6], and Omnilingual ASR has no Tuvan row [7]. We found no Tuvan speech dataset.

## Machine translation

**Products.** Google Translate added Tuvan on 27 June 2024 [2][3]. The Google Cloud Translation language page (November 2026) does not list Tuvan [4], so the API may not offer it; we did not check this further. Yandex Translate supports Tuvan [11]. Microsoft does not list Tuvan [5]. We found no quality numbers for these products.

**Research.** SLONE published NLLB-200-600M models fine-tuned for Russian → Tuvan, with an extended vocabulary, trained on tyvan.ru data; CC BY-NC 4.0. The model cards report no scores [12]. A journal article describes an AI translation system for teaching Tuvan; we did not read it [13].

**Indirect benchmark.** For other Turkic languages of Russia (Bashkir, Kazakh, Kyrgyz, Tatar, Chuvash), 2026 studies report chrF++ of about 40 to 50 for fine-tuned NLLB or prompted DeepSeek-V3.2 [14]. These are different languages; they only show what may be possible with 100,000 to 1 million sentence pairs. chrF++ cannot be compared across languages.

We found no test of GPT, Claude or Gemini translating into Tuvan.

## AI projects

- tyvan.ru corpus and Agisight datasets [10].
- SLONE NLLB Russian–Tuvan models [12].
- FLORES-Tuvan (Kuzhuget, Mongush, Oorzhak; 2024) [8].
- ai-forever lists an mGPT model for Tuvan, next to its Kalmyk and Buryat models [15].

## Recommendation

To translate into Tuvan today, use Google Translate or Yandex as a baseline, and compare them with a frontier LLM. Translate from Russian where possible, because the parallel data and the FLORES-Tuvan set are Russian–Tuvan [8][10]. A native speaker must post-edit all output.

Confidence: **low**. The products exist, but there is no published quality test.

First test: use 100 sentences from FLORES-Tuvan [8] (Russian → Tuvan). Translate with Google Translate, Yandex, one or two frontier LLMs and the SLONE model. Score with chrF++. Then translate 30 sentences of Buddhist prose and ask two native speakers to rank the outputs and check Buddhist terms.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Tuvan. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (1)

- [NLLB Russian-Tuvan models](https://huggingface.co/slone/nllb-rus-tyv-v2-extvoc) (SLONE): NLLB-200-600M with an extended vocabulary, fine-tuned for Russian-Tuvan translation. No scores published.

**Datasets** (1)

- [Tuvan-Russian parallel 50k](https://huggingface.co/datasets/Agisight/tyvan-russian-parallel-50k) (Agisight (tyvan.ru)): 50,000 Russian-Tuvan sentence pairs taken from the tyvan.ru corpus.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: Tuvan language](https://en.wikipedia.org/wiki/Tuvan_language), read 2026-11-17
2. [Google Translate Help: more than 100 new languages](https://support.google.com/translate/answer/15139004?hl=en), read 2026-11-17
3. [RFE/RL, 28 June 2024: Google Translate adds 110 languages](https://www.rferl.org/a/google-translate-adds-110-languages-including-mother-tongues-russia/33012893.html), read 2026-11-17
4. [Google Cloud Translation: language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
5. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
6. [openai/whisper tokenizer.py (language list)](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
7. [Omnilingual ASR per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
8. [FLORES extended to Tuvan, WMT 2024](https://aclanthology.org/2024.wmt-1.46), read 2026-11-17
9. [The Moscow Times, 2023](https://www.themoscowtimes.com/all/80432), read 2026-11-17
10. [Agisight/tyvan-russian-parallel-50k](https://huggingface.co/datasets/Agisight/tyvan-russian-parallel-50k), read 2026-11-17
11. [www1.ru: Yandex adds Buryat, 25 October 2025](https://www1.ru/en/news/2025/10/25/iandeks-rassiriaet-gorizonty-v-perevodcike-osvoen-buriatskii-iazyk.html), read 2026-11-17
12. [slone/nllb-rus-tyv-v2-extvoc model card](https://huggingface.co/slone/nllb-rus-tyv-v2-extvoc), read 2026-11-17
13. [Using AI to develop a machine translation system for Tuvan (nit.tuva.asia)](https://nit.tuva.asia/nit/en/article/view/1297), read 2026-11-17
14. [Turkic low-resource MT, arXiv 2602.04442](https://arxiv.org/html/2602.04442v1), read 2026-11-17
15. [ai-forever/mGPT-1.3B-kalmyk model card](https://huggingface.co/ai-forever/mGPT-1.3B-kalmyk/raw/main/README.md), read 2026-11-17
