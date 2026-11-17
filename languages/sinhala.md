---
id: sinhala
title: Sinhala
kind: modern
group: Indic
countries: [Sri Lanka]
scripts: [Sinhala]
speakers: about 20 million (18 million first language; Wikipedia [1])
directory_names: [Sinhala]
resource_level: medium
google_translate: yes (year not verified)
recommendation: Google Translate or a frontier LLM with a Sinhala reviewer
confidence: medium
updated: 2026-11
contributors: []
---

# Sinhala

Sinhala is a main language of Sri Lanka and of Sri Lankan Theravada Buddhism. Sri Lankans also use its script to read Pali. Google Translate was the best system in the only human test we found (2024), but that test is old.

## Summary

| | |
| --- | --- |
| Where | Sri Lanka |
| Speakers | about 18 million first language, 2 million second language, 20 million total [1] |
| Script | Sinhala script |
| AI resources | medium |
| Google Translate | yes; NMT only in the Cloud API [2] |
| Microsoft Translator | yes (code si) [3] |
| Speech to text | Whisper lists Sinhala [4]; Meta Omnilingual ASR covers it [5] |
| Best evidence on translation quality | human evaluation, University of Moratuwa (2024) [6]; FLORES-200 (2023) [7] |

## Writing and text input

Sinhala has its own script, which is in Unicode. Correct rendering needs the zero-width joiner (ZWJ) character. In the 2024 Moratuwa study, Bing and Claude dropped this character in their output [6]. Check for it in any Sinhala pipeline.

OCR: a Sinhala and Pali OCR model and its data (pathnirvana) are listed in the Directory below.

## Data

- General text: the SinLlama team cleaned and deduplicated MADLAD-400 and CulturaX into 10,730,154 Sinhala sentences (about 304 million tokens), shared as `polyglots/MADLAD_CulturaX_cleaned` [8]. The license is not stated in the paper.
- Buddhist text: Tipitaka.lk, SiPaKosa and Daham Danuma are listed in the Directory below. The license of the Buddha Jayanti Tipitaka is not verified.
- Palm-leaf manuscripts: not researched.

## Speech

- OpenAI Whisper lists Sinhala (si) [4]. We found no published error rate.
- Meta Omnilingual ASR (November 2025) reports a character error rate of 7.2 for Sinhala, with 225.4 hours of training audio [5]. Test sets differ by language, so use this only as a sign of support.
- OpenSLR SLR52 is a crowd-sourced Sinhala speech corpus by Google (2016–2018) with checked transcripts. The page does not give the number of hours; the license is in a LICENSE.txt file [9].

## Machine translation

**Support.** Google Translate supports Sinhala (NMT only in the Cloud API) [2]. Microsoft Translator supports Sinhala [3]. Meta NLLB-200 covers Sinhala [7]. IndicTrans2 does not cover Sinhala [10].

**Human evaluation (small; between a benchmark and a report): University of Moratuwa, 2024 [6].** About 100-word texts, 6 reviewers, scale 0 to 5 (higher is better).

| System | English to Sinhala | Sinhala to English |
| --- | --- | --- |
| Google Translate | 3.7 | 3.6 |
| Bing (Microsoft) | 3.4 | not given here |
| Llama 3 70B | 3.1 | not given here |
| GPT-4o | 2.6 | 3.5 |
| Claude 3 Sonnet (free) | 2.4 | 3.4 |
| Mistral Large | 0.8 | not given here |

No system averaged above 4. Gemini was left out because it "could not generate Sinhala" at that time [6].

**Benchmark: FLORES-200 devtest, English to Sinhala, chrF++ (higher is better), 2023 [7].** Google Translate 51.2; NLLB-200 MoE 43.8; ChatGPT (gpt-3.5) 5-shot 20.1; 0-shot 19.5. A copy of the NLLB-200 metrics file (model not verified) gives 43.9 [11].

Both tests are old (2023 and 2024). Newer models (GPT-5.x, Claude 4.x and 5.x, Gemini 3) may be much better, but we found no newer score. chrF++ can only be compared between systems in the same language and direction.

## AI projects

- SinLlama (University of Moratuwa and partners): Llama-3-8B extended for Sinhala. It beats the base model on three Sinhala classification tasks (for example, news category F1 86.40 vs 61.14). It was not tested on translation. Model: huggingface.co/polyglots/SinLlama_v01; the license is not stated in the paper [8].
- SinhalaMMLU (EMNLP 2025), a Sinhala understanding benchmark, appeared in our search. We did not open it.

## Recommendation

To translate into Sinhala today, use Google Translate as a safe baseline, or a current frontier model, and always have a Sinhala reviewer. Confidence is medium that Google is a safe baseline (it led both the 2023 and 2024 tests). Confidence is low for any ranking among current LLMs.

Test first: FLORES+ devtest, English to Sinhala, with chrF++, on Google and two or three current models. Add native review of 50 sentences and a Buddhist sample (for example, 20 short dhamma passages with standard Sinhala Buddhist terms). Check every output for the zero-width joiner. Sinhala is not yet measured on the BuddhistAI leaderboard.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Sinhala. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (3)

- [Tipitaka.lk](https://tipitaka.lk/) (Path Nirvana): The Buddha Jayanthi Tipitaka of Sri Lanka with its Sinhala translation, plus other Pali editions.
- [Sinhala and Pali OCR model](https://huggingface.co/pathnirvana/sinhala-pali-ocr-lightonocr-1b) (Path Nirvana): OCR model for old Sinhala and Pali prints, trained on its own open dataset.
- [SinLlama](https://huggingface.co/polyglots/SinLlama_v01) (University of Moratuwa and partners (polyglots)): Llama-3-8B extended with Sinhala vocabulary and further training on Sinhala text. Base model, not instruction-tuned. Not Buddhist-specific.

**Datasets** (3)

- [Daham Danuma](https://github.com/sdkaluwitharana/daham-danuma) (sdkaluwitharana (community)): Open bank of multiple-choice questions for Dhamma school students in Sri Lanka.
- [SiPaKosa](https://github.com/RanxduG/SiPaKosa-Dataset) (RanxduG (community)): Corpus of canonical and classical Buddhist texts in Sinhala and Pali.
- [Sinhala and Pali OCR data](https://huggingface.co/datasets/pathnirvana/sinhala-pali-ocr) (Path Nirvana): Old Sinhala and Pali prints with transcriptions.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: Sinhala language](https://en.wikipedia.org/wiki/Sinhala_language), read 2026-11-17
2. [Google Cloud Translation: Language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
3. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
4. [OpenAI Whisper tokenizer.py (language list)](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py), read 2026-11-17
5. [Meta Omnilingual ASR, per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
6. [Jayakody and Dias 2024, arXiv 2407.21330](https://arxiv.org/pdf/2407.21330), read 2026-11-17
7. [Robinson et al. 2023, arXiv 2309.07423](https://arxiv.org/pdf/2309.07423), read 2026-11-17
8. [SinLlama, arXiv 2508.09115v3](https://arxiv.org/html/2508.09115v3), read 2026-11-17
9. [OpenSLR 52: Sinhala ASR corpus](https://openslr.org/resources/52/about.html), read 2026-11-17
10. [IndicTrans2, arXiv 2305.16307](https://arxiv.org/pdf/2305.16307), read 2026-11-17
11. [Copy of the NLLB-200 metrics file (Mara4444/MSc_Thesis)](https://raw.githubusercontent.com/Mara4444/MSc_Thesis/main/datasets/others/nllb_metrics.csv), read 2026-11-17
