---
id: lao
title: Lao
kind: modern
group: Southeast Asian
countries: [Laos, Thailand]
scripts: [Lao, Tham]
speakers: about 3.7 million first language and 0.8 million second language (2015; Wikipedia, no source named [1])
speakers_n: 3700000
speakers_year: 2015
speakers_source: https://en.wikipedia.org/wiki/Lao_language
speakers_basis: first-language speakers
directory_names: [Lao]
resource_level: medium
google_translate: yes
recommendation: Gemini (2.5 Pro or 3 Pro) with a glossary and native review
confidence: medium
updated: 2026-11
contributors: []
---

# Lao

Lao is the language of Theravada Buddhism in Laos and is close to the Isan speech of northeast Thailand. It has the fewest AI resources of the four national languages of mainland Southeast Asia. Large models can translate into Lao, but a native reviewer is needed.

## Summary

| | |
| --- | --- |
| Where | Laos; as "Isan" in northeast Thailand [1] |
| Speakers | 3.7 million first language (2015), 800,000 second language; the article names no source [1] |
| Script | Lao script; old Buddhist manuscripts often in Tham scripts [2] |
| AI resources | medium |
| Google Translate | yes; Google Cloud: Translation LLM and NMT [3] |
| Microsoft Translator | yes [4] |
| Speech to text | Whisper supports Lao [5]; Omnilingual ASR covers Lao [6] |
| Best evidence on translation quality | LaoBench: Gemini 2.5 Pro best closed model (2025) [7] |

## Writing and text input

Lao has its own Unicode script. Words are not separated by spaces. LaoBench had to use a Lao segmenter (LaoNLP) to compute BLEU [7]. For scoring, use chrF++ or a learned metric.

Isan in Thailand has a separate language code (`tts`). Lao, Isan and Thai are mutually intelligible [1]. When you test a model, check that its Lao output does not drift into Thai words or spelling.

Many Lao Buddhist manuscripts are not in modern Lao script. The Digital Library of Lao Manuscripts holds mostly Lao, Lan Na and Tai Lue traditions in Tham scripts [2]. We found no OCR model for Tham script.

## Data

- **Digital Library of Lao Manuscripts (DLLM)**: images of over 12,000 texts from the Preservation of Lao Manuscripts Programme (National Library of Laos, University of Passau, Staatsbibliothek zu Berlin). Images can be viewed and downloaded. There is no general license; ask before publication [2]. These are images, not machine-readable text.
- **Asian Language Treebank (ALT)**: about 20,000 English news sentences translated into Lao and 11 other languages; CC BY 4.0 [8].
- **WMT26 Chinese–Southeast Asian task** (2026): manually aligned Chinese–Lao data, monolingual data and a blind test set [9].
- **LaoBench**: more than 17,000 Lao test items, including Lao–Chinese–English translation. License not stated [7].

We found no machine-readable Lao Tipitaka dataset.

## Speech

Omnilingual ASR (Meta, November 2025) has a Lao character error rate of 6.6, with 184.8 hours of training data [6]. Test sets differ between languages, so do not compare languages with this number. We found no Lao Buddhist speech dataset.

## Machine translation

**Benchmarks.**

| System | Test | Direction | Metric | Score | Year |
| --- | --- | --- | --- | --- | --- |
| NLLB-200 (MoE) | FLORES-200 | English → Lao | chrF++ | 46.2 | 2023 [10] |
| Google Translate | FLORES-200 | English → Lao | chrF++ | 44.0 | 2023 [10] |
| ChatGPT (gpt-3.5), 5-shot | FLORES-200 | English → Lao | chrF++ | 21.5 | 2023 [10] |
| SeaLLMs 3 (7B) | FLORES-200 | English → Lao | chrF | 26.34 | 2024 [11] |

The 2023 results are old and do not show what newer models can do. chrF++ and BLEU numbers can only be compared between systems in the same language and direction. A higher Lao score than Thai score does not mean Lao output is better.

**LaoBench** (BAAI, Peking University and partners, November 2025) [7]:

- Translation BLEU, best closed model: Gemini 2.5 Pro (34.31 culture and history, 40.71 international affairs). Best open model, Qwen3-235B: 21.81.
- chrF++ for GPT-5-High, Gemini 2.5 Pro and Qwen3-Max was about 50 to 66.
- The authors call translation "a clear weakness for all models".
- Open-ended answers, win rate against GPT-5-High: Gemini 2.5 Pro about 51.5%, Claude Sonnet 4.5 about 50.3%, Claude Opus 4.1 about 49.3%. This is not a translation test.

No published test uses Buddhist text in Lao.

## AI projects

- Regional models that cover Lao: Gemma-SEA-LION-v4-27B-IT (AI Singapore, August 2025) [12], Sailor2 (Sea AI Lab, Apache-2.0) [13], SeaLLMs 3 [11].
- LaoBench (BAAI and partners) [7].
- We found no Lao Buddhist AI project.

## Recommendation

To translate into Lao today, use Gemini (2.5 Pro or 3 Pro) with a Buddhist glossary. Compare with GPT-5 or Claude, and keep Google Translate as a baseline. A native Lao reader with Buddhist training should review all output.

Confidence: **medium**. LaoBench is a direct 2025 test, but its translation scores are BLEU on general topics, and no test uses Buddhist text.

First test: take 50 to 100 sentences of Buddhist prose with a trusted Lao translation. Translate with Gemini, one other frontier model and Google Translate. Score with chrF++, and ask the reviewer to mark Thai words or Thai spelling in the Lao output.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Lao. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (2)

- [Digital Library of Lao Manuscripts](https://digital.crossasia.org/digital-library-of-lao-manuscripts/?lang=en) (National Library of Laos, University of Passau, Staatsbibliothek zu Berlin): Images of more than 12,000 Lao, Lan Na and Tai Lue manuscripts from the Preservation of Lao Manuscripts Programme, with downloadable sets.
- [Gemma-SEA-LION-v4-27B-IT](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT) (AI Singapore): Gemma 3 based 27B chat model for Southeast Asian languages, including Burmese, Khmer, Lao, Thai and Vietnamese. Not Buddhist-specific.

**Datasets** (1)

- [Asian Language Treebank (ALT)](https://huggingface.co/datasets/alt) (NICT and partners): About 20,000 English Wikinews sentences translated into 12 Asian languages, including Thai, Lao, Khmer and Burmese. Not Buddhist-specific.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: Lao language](https://en.wikipedia.org/wiki/Lao_language), read 2026-11-17
2. [Digital Library of Lao Manuscripts](https://digital.crossasia.org/digital-library-of-lao-manuscripts/?lang=en), read 2026-11-17
3. [Google Cloud Translation: language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
4. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
5. [openai/whisper tokenizer.py (language list)](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
6. [Omnilingual ASR per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
7. [LaoBench, arXiv 2511.11334](https://arxiv.org/html/2511.11334v3), read 2026-11-17
8. [Asian Language Treebank dataset card](https://huggingface.co/datasets/alt/blob/main/README.md), read 2026-11-17
9. [WMT26 Chinese–Southeast Asian shared task, ACL Anthology](https://aclanthology.org/2026.wmt-main.55/), read 2026-11-17
10. [Robinson et al. 2023, ChatGPT MT, arXiv 2309.07423, Table 11](https://arxiv.org/pdf/2309.07423), read 2026-11-17
11. [SeaLLMs 3, arXiv 2407.19672](https://arxiv.org/html/2407.19672v1), read 2026-11-17
12. [Gemma-SEA-LION-v4-27B-IT readme (mirror)](https://featherless.ai/models/aisingapore/Gemma-SEA-LION-v4-27B-IT/readme), read 2026-11-17
13. [Sea AI Lab: Sailor2](https://sail.sea.com/blog/articles/55), read 2026-11-17
