---
id: thai
title: Thai
kind: modern
group: Southeast Asian
countries: [Thailand]
scripts: [Thai]
speakers: about 71 million incl. second-language speakers (2024; Wikipedia [1])
directory_names: [Thai]
resource_level: high
google_translate: yes
recommendation: Frontier LLM with a Buddhist glossary and monastic review
confidence: medium
updated: 2026-11
contributors: []
---

# Thai

Thai is the main language of Theravada Buddhism in Thailand. It is the best-resourced of the Theravada languages of mainland Southeast Asia. Large AI models write good general Thai; the main risk is Buddhist terms.

## Summary

| | |
| --- | --- |
| Where | Thailand |
| Speakers | 27 million first language, 44 million second language, 71 million in total (2024) [1] |
| Script | Thai script, no spaces between words |
| AI resources | high |
| Google Translate | yes; Google Cloud: Translation LLM and NMT [3] |
| Microsoft Translator | yes, with the "LLM translation" option [4] |
| Speech to text | Whisper supports Thai [5]; open Thai models exist (Thonburian Whisper) [6] |
| Best evidence on translation quality | WMT24++: frontier LLMs ranked highest for Thai (2025) [7] |

## Writing and text input

Thai has its own Unicode script. There are no spaces between words, so word segmentation is needed for search and for word-based scores such as BLEU. For example, the LaoBench authors needed a segmenter to score Lao, a related language, with BLEU [2].

OCR: Typhoon OCR (SCB 10X, report January 2026) is an open model family for Thai documents. On SCB 10X's own Thai tests, version 1.5 had an average BLEU of 0.644, Gemini 2.5 Pro 0.605 and GPT-5 0.459. This is a vendor evaluation, not an independent test [8].

## Data

Thai Buddhist text is well digitized. Several sets are already in the Directory (Thai Tipitaka editions, Nak Tham exams).

- **BUDSIR** (Mahidol University): Pali Tipitaka in Thai script with search, since 1988; commentaries added in 1991 (50,189 pages in total). The history page does not mention a Thai translation [9].
- **Thai Tipitaka program** (SourceForge): Royal, Mahachula and Mahamakut Thai editions and two Pali editions; GPL-2.0; last update June 2019 [10]. The Thai translations aligned with the Pali text are the main source of Pali–Thai parallel text. Licenses of the editions themselves are not clear.
- **Tipiṭaka Sajjhāya** (World Tipiṭaka Foundation, Bangkok): Pali Tipitaka in Roman script with recitation notation; "All Rights Reserved" [11].
- **Asian Language Treebank (ALT)**: about 20,000 English news sentences translated into 12 Asian languages, including Thai; CC BY 4.0 [12].

## Speech

- **Thonburian Whisper** (Mahidol University, biodatlab): Whisper models fine-tuned for Thai, first released December 2022; distilled models trained on under 1,500 hours [6]. We did not read its error rates or license.
- **Omnilingual ASR** (Meta, November 2025): Thai character error rate 4.9, with 514.9 hours of training data [13]. These test sets differ between languages, so do not compare languages with this number.

## Machine translation

**Benchmarks.**

| System | Test | Direction | chrF++ | Year |
| --- | --- | --- | --- | --- |
| Google Translate | FLORES-200 | English → Thai | 49.7 | 2023 [14] |
| ChatGPT (gpt-3.5), 5-shot | FLORES-200 | English → Thai | 43.2 | 2023 [14] |
| NLLB-200 (MoE) | FLORES-200 | English → Thai | 42.7 | 2023 [14] |
| SeaLLMs 3 (7B) | FLORES-200, chrF | English → Thai | 41.52 | 2024 [15] |

The 2023 results are old. They do not show what 2025–2026 models can do. chrF++ and BLEU numbers can only be compared between systems in the same language and direction, not between languages.

Newer evidence: in WMT24++ (Google and Unbabel, 2025), frontier LLMs (o1, Claude, Gemini) ranked highest for every language, including Thai, above Google Translate [7]. We did not read the Thai numbers. In MiLMMT-46 (February 2026), the average English → 46 languages (including Thai) on FLORES+ was: Gemini 3 Pro spBLEU 42.42, GPT-5 38.42, NLLB-54.5B 38.05 [16]. This is an average over languages, not a Thai result.

**Vendor claim.** Typhoon Translate 1.5 (SCB 10X, 4B, Thai ↔ English only) was judged by GPT-4o-mini against systems that are not named. The card shows no scores, and its license information is not consistent [17].

No published test uses Buddhist text in Thai.

## AI projects

- **Typhoon** (SCB 10X): Thai LLMs, translation, OCR and speech models [8][17].
- **Pathumma** (NECTEC): Thai and English 4B model, Apache-2.0 [18].
- **Thai national LLM**: NSTDA and Siam AI signed an agreement on 6 June 2025; a 7B model is planned [19].
- Regional models that cover Thai: Gemma-SEA-LION-v4-27B-IT (AI Singapore, August 2025) [20], Sailor2 (Sea AI Lab, Apache-2.0) [21], SeaLLMs 3 [15].
- Buddhist: "Phra Maha AI", described as Thailand's first virtual monk (January 2022); the builder is not named [22].

## Recommendation

To translate into Thai today, use a frontier LLM (Gemini, GPT or Claude) with a Buddhist glossary. Keep Google Translate as a baseline and Typhoon Translate as an open option for English → Thai. A monk or Pali-trained translator should review doctrinal terms.

Confidence: **medium**. Benchmarks say frontier LLMs lead for Thai [7], but we did not read Thai numbers, and no test uses Buddhist text.

First test: take about 100 sentences of Buddhist prose that already have a human Thai translation (for example from the Mahachula edition [10]). Translate them with two or three frontier models, Google Translate and Typhoon. Score with chrF++ and ask a reviewer to check the Buddhist terms.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Thai. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (7)

- [Thai Tipitaka program](https://sourceforge.net/p/thaitipitaka) (ajsun and bistechn (community)): Desktop program with the Thai Royal, Mahachula and Mahamakut Thai Tipitaka editions and two Pali editions in Thai script.
- [BUDSIR](https://www.mahidol.ac.th/budsir/history.htm) (Mahidol University): Search system for the Pali Tipitaka and commentaries in Thai and Roman script, in use since 1988.
- [Tipitaka Sajjhaya](https://sajjhaya.org/node/20) (World Tipitaka Foundation (Bangkok)): The Sixth Council Pali Tipitaka in Roman script, with notation for recitation and audio recordings.
- [Typhoon OCR](https://huggingface.co/scb10x/typhoon-ocr1.5-2b) (SCB 10X): Open vision-language OCR models for Thai and English documents. Output is Markdown with tables and figures.
- [Thonburian Whisper](https://biodatlab.github.io/blog/thonburian-whisper-2024) (Mahidol University (biodatlab)): Whisper models fine-tuned for Thai speech recognition, including smaller distilled versions.
- [Gemma-SEA-LION-v4-27B-IT](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT) (AI Singapore): Gemma 3 based 27B chat model for Southeast Asian languages, including Burmese, Khmer, Lao, Thai and Vietnamese. Not Buddhist-specific.
- [BuddhistAI benchmarks](https://buddhistai.github.io/buddhist-benchmarks/) (BuddhistAI): Open benchmarks and leaderboards for Buddhist tasks. Ranks models and skills by top performance and best value.

**Datasets** (6)

- [Thai Buddhist Studies Exam (Nak Tham)](https://huggingface.co/datasets/biodatlab/thai_buddhist_studies_exam) (Mahidol University (biodatlab)): About 4,100 multiple-choice questions from the Thai national Dhamma exams (2020, 2022, 2023), three levels. Imported into BuddhistBench.
- [BuddhistBench](https://github.com/BuddhistAI/buddhist-bench) (BuddhistAI): Question and answer benchmark on Buddhist knowledge across traditions and languages, built from expert-written and exam sets.
- [Thai Tipitaka and commentaries (MBU edition)](https://huggingface.co/datasets/uisp/tripitaka-mbu) (uisp (community)): The Thai Tipitaka with commentaries, Mahamakut edition, 91 volumes, one file per page.
- [Pali Tipitaka in Thai script](https://huggingface.co/datasets/uisp/pali-tripitaka-thai-script-siamrath-version) (uisp (community)): The Pali Tipitaka (Siamrath edition) in Thai script, with a matching commentary set.
- [Asian Language Treebank (ALT)](https://huggingface.co/datasets/alt) (NICT and partners): About 20,000 English Wikinews sentences translated into 12 Asian languages, including Thai, Lao, Khmer and Burmese. Not Buddhist-specific.
- [Thai Dhamma books](https://huggingface.co/datasets/uisp/dhamma-scholar-book) (uisp (community)): Thai Dhamma study books, with a second set for the general public.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: Thai language](https://en.wikipedia.org/wiki/Thai_language), read 2026-11-17
2. [LaoBench, arXiv 2511.11334 (word segmentation for scoring)](https://arxiv.org/html/2511.11334v3), read 2026-11-17
3. [Google Cloud Translation: language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
4. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
5. [openai/whisper tokenizer.py (language list)](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
6. [biodatlab: Thonburian Whisper 2024](https://biodatlab.github.io/blog/thonburian-whisper-2024), read 2026-11-17
7. [WMT24++, arXiv 2502.12404](https://arxiv.org/html/2502.12404v1), read 2026-11-17
8. [Typhoon OCR report, arXiv 2601.14722](https://arxiv.org/html/2601.14722), read 2026-11-17
9. [Mahidol University: BUDSIR history](https://www.mahidol.ac.th/budsir/history.htm), read 2026-11-17
10. [SourceForge: Thai Tipitaka](https://sourceforge.net/p/thaitipitaka), read 2026-11-17
11. [Tipiṭaka Sajjhāya](https://sajjhaya.org/node/20), read 2026-11-17
12. [Asian Language Treebank dataset card](https://huggingface.co/datasets/alt/blob/main/README.md), read 2026-11-17
13. [Omnilingual ASR per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
14. [Robinson et al. 2023, ChatGPT MT, arXiv 2309.07423, Table 11](https://arxiv.org/pdf/2309.07423), read 2026-11-17
15. [SeaLLMs 3, arXiv 2407.19672](https://arxiv.org/html/2407.19672v1), read 2026-11-17
16. [MiLMMT-46, arXiv 2602.11961](https://www.alphaxiv.org/abs/2602.11961.md), read 2026-11-17
17. [Typhoon Translate 1.5 model card](https://huggingface.co/scb10x/typhoon-translate1.5-4b), read 2026-11-17
18. [NECTEC Pathumma-llm-4b-4.0.0](https://huggingface.co/nectec/Pathumma-llm-4b-4.0.0), read 2026-11-17
19. [The Thaiger: Thailand invests 300 million baht in Thai AI language model](https://thethaiger.com/news/business/thailand-invests-300-million-baht-in-thai-ai-language-model), read 2026-11-17
20. [Gemma-SEA-LION-v4-27B-IT readme (mirror)](https://featherless.ai/models/aisingapore/Gemma-SEA-LION-v4-27B-IT/readme), read 2026-11-17
21. [Sea AI Lab: Sailor2](https://sail.sea.com/blog/articles/55), read 2026-11-17
22. [The Thaiger: Thailand's first virtual monk](https://thethaiger.com/news/national/thailands-first-virtual-monk-targets-at-new-generation-buddhists), read 2026-11-17
