---
id: khmer
title: Khmer
kind: modern
group: Southeast Asian
countries: [Cambodia]
scripts: [Khmer]
speakers: about 21 million incl. second-language speakers (2019 and 2024; Wikipedia, no source named [1])
speakers_n: 21000000
speakers_year: 2024
speakers_source: https://en.wikipedia.org/wiki/Khmer_language
directory_names: [Khmer]
resource_level: medium
google_translate: yes
recommendation: Frontier LLM or Google Translate after a side-by-side test
confidence: low
updated: 2026-11
contributors: []
---

# Khmer

Khmer is the language of Theravada Buddhism in Cambodia. Large AI models and Google Translate support it, but there is no recent Khmer translation benchmark. Most Khmer Buddhist material is manuscript images, not text.

## Summary

| | |
| --- | --- |
| Where | Cambodia |
| Speakers | 19 million first language (2019), 1 million second language (2024); the article names no source [1] |
| Script | Khmer script, no spaces between words |
| AI resources | medium |
| Google Translate | yes; Google Cloud: Translation LLM and NMT [2] |
| Microsoft Translator | yes [3] |
| Speech to text | Whisper supports Khmer [4]; small open speech sets [5] |
| Best evidence on translation quality | FLORES-200, Google Translate and NLLB (2023) [6] |

## Writing and text input

Khmer has its own Unicode script. Words are not separated by spaces, so word-based scores such as BLEU need a fixed segmenter. Use chrF++ or a learned metric instead.

OCR: there are community Khmer OCR models (for example "Chakkhu" and "kiri-ocr") and a Khmer scene-text benchmark (KhmerST). We saw these only in search results and did not test them. An older research paper describes a sequence-to-sequence Khmer OCR model [7].

## Data

- **Khmer Manuscript Heritage Project** (BDRC with Digital Divide Data and FEMC/EFEO): since 2019, digital copies of 11,596 manuscripts, "more than 1.4 million pages", and 757,507 pages of FEMC microfilms. Images only; no transcription is mentioned; license not stated [8].
- **5000-years.org**: Khmer Buddhist site (founded 2012) with books, MP3 Dhamma talks, chanting and videos, and a link to an online Khmer Tipitaka. No license stated [9].
- **Asian Language Treebank (ALT)**: about 20,000 English news sentences translated into Khmer and 11 other languages; CC BY 4.0 [10].
- **WMT26 Chinese–Southeast Asian task** (2026): aligned Chinese–Khmer data and a blind test set [11].

We did not find a machine-readable Khmer Tipitaka dataset. Khmer Buddhist text for AI would need OCR of the manuscript images first.

## Speech

- **seanghay/km-speech-corpus**: about 10.4 hours, 14,943 clips, CC BY 4.0; the source of the audio is not stated [5]. Other small Khmer speech sets exist (search results only).
- **Omnilingual ASR** (Meta, November 2025): Khmer character error rate 4.8, with 197.4 hours of training data [12]. Test sets differ between languages, so do not compare languages with this number.
- 5000-years.org has Khmer Dhamma talk audio [9]. It could become a test set, but only with permission.

## Machine translation

**Benchmarks.**

| System | Test | Direction | Metric | Score | Year |
| --- | --- | --- | --- | --- | --- |
| Google Translate | FLORES-200 | English → Khmer | chrF++ | 40.3 | 2023 [6] |
| NLLB-200 (MoE) | FLORES-200 | English → Khmer | chrF++ | 36.4 | 2023 [6] |
| ChatGPT (gpt-3.5), 0-shot | FLORES-200 | English → Khmer | chrF++ | 21.5 | 2023 [6] |
| SeaLLMs 3 (7B) | FLORES-200 | English → Khmer | chrF | 27.30 | 2024 [13] |

These results are old (2023–2024). They do not show what 2025–2026 frontier models can do. chrF++ numbers can only be compared between systems in the same language and direction, not between languages.

Newer evidence is only indirect. In MiLMMT-46 (February 2026), the average English → 46 languages (including Khmer) on FLORES+ ranked Gemini 3 Pro first, then MiLMMT-46-12B, GPT-5 and NLLB-54.5B; Google Translate was also above MiLMMT [14]. We could not read the Khmer numbers. We found no Khmer-specific LLM translation benchmark and no test with Buddhist text.

## AI projects

- **Bayon** (attentionlab): a 100-million-parameter Khmer model trained from scratch, Apache-2.0, tested on 201 Khmer history and culture questions [15].
- Regional models that cover Khmer: Gemma-SEA-LION-v4-27B-IT (AI Singapore, August 2025) [16], Sailor2 (Sea AI Lab, Apache-2.0) [17], SeaLLMs 3 [13].
- We found no Khmer Buddhist AI project.

## Recommendation

To translate into Khmer today, compare a frontier LLM (Gemini first, then GPT-5 or Claude) with Google Translate on your own sample, and use the better one with a Buddhist glossary. Gemma-SEA-LION-v4-27B-IT is an open option. A native reviewer with Buddhist training must check all output.

Confidence: **low**. The only Khmer-specific numbers are from 2023, and the newer evidence is an average over many languages.

First test: take 50 to 100 sentences of Buddhist prose with a trusted Khmer translation. Translate them with two frontier models and Google Translate. Score with chrF++ and ask a reviewer to rank the outputs and mark wrong Buddhist terms.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Khmer. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (3)

- [5000-years.org](https://5000-years.org/en/books/all) (5000-years.org): Khmer Buddhist site with Dhamma books, recorded Dhamma talks and chanting, videos, and a link to an online Khmer Tipitaka.
- [Khmer Manuscript Heritage Project](https://khmer-manuscripts.bdrc.io/) (BDRC with Digital Divide Data and FEMC/EFEO): Digital copies of 11,596 Khmer manuscripts (more than 1.4 million pages), plus digitized FEMC microfilms.
- [Gemma-SEA-LION-v4-27B-IT](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT) (AI Singapore): Gemma 3 based 27B chat model for Southeast Asian languages, including Burmese, Khmer, Lao, Thai and Vietnamese. Not Buddhist-specific.

**Datasets** (2)

- [Asian Language Treebank (ALT)](https://huggingface.co/datasets/alt) (NICT and partners): About 20,000 English Wikinews sentences translated into 12 Asian languages, including Thai, Lao, Khmer and Burmese. Not Buddhist-specific.
- [Khmer speech corpus](https://huggingface.co/datasets/seanghay/km-speech-corpus) (seanghay (community)): About 10.4 hours of Khmer speech in 14,943 clips.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: Khmer language](https://en.wikipedia.org/wiki/Khmer_language), read 2026-11-17
2. [Google Cloud Translation: language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
3. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
4. [openai/whisper tokenizer.py (language list)](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
5. [seanghay/km-speech-corpus dataset card](https://huggingface.co/datasets/seanghay/km-speech-corpus/blob/main/README.md), read 2026-11-17
6. [Robinson et al. 2023, ChatGPT MT, arXiv 2309.07423, Table 11](https://arxiv.org/pdf/2309.07423), read 2026-11-17
7. [Khmer OCR with sequence-to-sequence models, arXiv 2106.10875](https://ar5iv.labs.arxiv.org/html/2106.10875), read 2026-11-17
8. [BDRC: Khmer Manuscript Heritage Project](https://khmer-manuscripts.bdrc.io/scripts/static//aboutkm.en.html), read 2026-11-17
9. [5000-years.org](https://5000-years.org/en/books/all), read 2026-11-17
10. [Asian Language Treebank dataset card](https://huggingface.co/datasets/alt/blob/main/README.md), read 2026-11-17
11. [WMT26 Chinese–Southeast Asian shared task, ACL Anthology](https://aclanthology.org/2026.wmt-main.55/), read 2026-11-17
12. [Omnilingual ASR per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
13. [SeaLLMs 3, arXiv 2407.19672](https://arxiv.org/html/2407.19672v1), read 2026-11-17
14. [MiLMMT-46, arXiv 2602.11961](https://www.alphaxiv.org/abs/2602.11961.md), read 2026-11-17
15. [attentionlab/bayon model card](https://huggingface.co/attentionlab/bayon), read 2026-11-17
16. [Gemma-SEA-LION-v4-27B-IT readme (mirror)](https://featherless.ai/models/aisingapore/Gemma-SEA-LION-v4-27B-IT/readme), read 2026-11-17
17. [Sea AI Lab: Sailor2](https://sail.sea.com/blog/articles/55), read 2026-11-17
