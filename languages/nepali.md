---
id: nepali
title: Nepali
kind: modern
group: Indic
countries: [Nepal, India, Bhutan]
scripts: [Devanagari]
speakers: about 32 million (19 million first language; Wikipedia [1])
directory_names: [Nepali]
resource_level: medium
google_translate: yes (year not verified)
recommendation: Google Translate or a frontier LLM; IndicTrans2 as open option
confidence: medium
updated: 2026-11
contributors: []
---

# Nepali

Nepali is the main language of Nepal, the country of the Buddha's birthplace. Buddhist communities in Nepal use it for teaching and daily life. Nepali has good general AI support, but no test uses Buddhist text.

## Summary

| | |
| --- | --- |
| Where | Nepal; also India and Bhutan |
| Speakers | about 19 million first language, 14 million second language, 32 million total [1] |
| Script | Devanagari |
| AI resources | medium |
| Google Translate | yes; Translation LLM and NMT in the Cloud API [2] |
| Microsoft Translator | yes (code ne) [3] |
| Speech to text | Whisper lists Nepali [4]; Meta Omnilingual ASR covers it [5] |
| Best evidence on translation quality | FLORES-200, NLLB and ChatGPT, 2023 [6] |

## Writing and text input

Nepali uses the Devanagari script, which is in Unicode. We did not verify OCR support for printed Nepali in this research.

Handwritten Old Nepali: a 2025 study built a handwriting recognition pipeline (TrOCR-large encoder) for Old Nepali Devanagari manuscripts. It reached a 4.9% character error rate, but only about 34% of lines were fully correct. Google Cloud Vision "performed poorly" on the same material (no number given). The manuscript data is confidential; the code is at github.com/anjalisarawgi/nepOCR [7].

## Data

- Parallel data: IndicTrans2 was trained on about 1.69 million English–Nepali pairs [8].
- Manuscripts and documents: Documenta Nepalica (Heidelberg Academy) holds Old Nepali documents used in the study above [7]. We did not open it.
- Web corpus sizes (FineWeb-2 and others) and Nepali–English corpus sizes: not verified.
- We found no Buddhist text corpus in Nepali in this research.

## Speech

- OpenAI Whisper lists Nepali (ne) [4]. We found no published error rate.
- Meta Omnilingual ASR (November 2025) reports a character error rate of 12.3 for npi_Deva (24.5 hours of training audio) and 6.5 for nep_Deva (11.3 hours) [5]. Test sets differ by language, so use these only as signs of support.
- OpenSLR Nepali speech sets: not verified.

## Machine translation

**Support.** Google Translate supports Nepali, and in the Cloud API it is in both the Translation LLM and NMT [2]. Microsoft Translator supports Nepali [3]. IndicTrans2 (AI4Bharat) covers Nepali (npi_Deva) and aims at permissive licenses, unlike NLLB, which is CC-BY-NC [8]. Meta NLLB-200 covers Nepali [6].

**Benchmark: FLORES-200 devtest, English to Nepali, chrF++ (higher is better).**

| System | Score | Year | Source |
| --- | --- | --- | --- |
| NLLB-200 MoE | 45.5 | 2022 model, tested 2023 | [6] |
| NLLB-200 (copies of the official file, model not verified) | 46.3 and 49.0 | 2022 | [9] [10] |
| ChatGPT (gpt-3.5) 0-shot | 39.5 | 2023 | [6] |
| ChatGPT (gpt-3.5) 5-shot | 39.3 | 2023 | [6] |

Google Translate was not scored for Nepali in that study [6]. These results are from 2023. Newer frontier models are likely better, but we found no recent public score. chrF++ can only be compared between systems in the same language and direction.

## AI projects

- Kathmandu University ILPRL: speech work in Nepal, including the Newari speech corpus Nwāchā Munā (2026), where a zero-shot Nepali model was one of the baselines [11].
- IndicTrans2 (AI4Bharat): open MT models that include Nepali [8].
- nepOCR (LMU Munich and Heidelberg Academy, 2025): Old Nepali handwriting recognition [7].

## Recommendation

To translate into Nepali today, use Google Translate or a current frontier model, with a Nepali reviewer for Buddhist terms. If you need an open model with a permissive license, test IndicTrans2. Confidence is medium: all systems support Nepali, but the only scores are from 2023 and none use Buddhist text.

Test first: FLORES+ devtest, English to Nepali, with chrF++, on Google, IndicTrans2 and two current models. Add a Buddhist sample (for example, 20 to 50 short passages from a teaching, with a glossary of Buddhist terms), reviewed by a native speaker. Nepali is not yet measured on the BuddhistAI leaderboard.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Nepali. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (1)

- [Nepalese-German Manuscript Cataloguing Project (NGMCP)](https://ngmcp.fdm.uni-hamburg.de/mediawiki/index.php/NGMCP) (University of Hamburg with the National Archives of Nepal): Catalogue of the Nepalese manuscripts that the Nepal-German Manuscript Preservation Project microfilmed (more than 114,500 items in Sanskrit, Newari, Nepali and other languages).

**Datasets** (0)

None listed yet.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: Nepali language](https://en.wikipedia.org/wiki/Nepali_language), read 2026-11-17
2. [Google Cloud Translation: Language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
3. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
4. [OpenAI Whisper tokenizer.py (language list)](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py), read 2026-11-17
5. [Meta Omnilingual ASR, per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
6. [Robinson et al. 2023, arXiv 2309.07423](https://arxiv.org/pdf/2309.07423), read 2026-11-17
7. [Sarawgi, Garces Arias and Zotter, Old Nepali HTR, arXiv 2512.17111, 2025-12-18](https://arxiv.org/html/2512.17111v1), read 2026-11-17
8. [IndicTrans2, arXiv 2305.16307](https://arxiv.org/pdf/2305.16307), read 2026-11-17
9. [Copy of the NLLB-200 metrics file (Mara4444/MSc_Thesis)](https://raw.githubusercontent.com/Mara4444/MSc_Thesis/main/datasets/others/nllb_metrics.csv), read 2026-11-17
10. [Copy of the NLLB-200 metrics file (XMUDeepLIT/RobustNMT-ISDST)](https://raw.githubusercontent.com/XMUDeepLIT/RobustNMT-ISDST/main/examples/m2m_100/metrics.csv), read 2026-11-17
11. [Nwāchā Munā, arXiv 2603.07554v2](https://arxiv.org/html/2603.07554), read 2026-11-17
