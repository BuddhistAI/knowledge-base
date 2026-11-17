---
id: burmese
title: Burmese
kind: modern
group: Southeast Asian
countries: [Myanmar]
scripts: [Myanmar]
speakers: about 33 million first language and 10 million second language (2019; Wikipedia [1])
directory_names: [Burmese, Shan, Mon]
resource_level: medium
google_translate: yes
recommendation: Gemini 2.5 Pro or newer with Unicode checks and native review
confidence: medium
updated: 2026-11
contributors: []
---

# Burmese

Burmese is the language of Theravada Buddhism in Myanmar. There is a direct 2026 benchmark for translation into Burmese, and Gemini 2.5 Pro was best on it. Old Burmese web text often uses the Zawgyi encoding, not Unicode.

## Summary

| | |
| --- | --- |
| Where | Myanmar |
| Speakers | 33 million first language (2019; Ethnologue per the article: 32.9 million), 10 million second language [1] |
| Script | Myanmar script; much legacy text in Zawgyi encoding [2] |
| AI resources | medium |
| Google Translate | yes; Google Cloud: Translation LLM and NMT [3] |
| Microsoft Translator | yes [4] |
| Speech to text | Whisper supports Burmese [5]; Omnilingual ASR covers it [6] |
| Best evidence on translation quality | BURMESE-SAN: Gemini 2.5 Pro best in translation (2026) [7] |

## Writing and text input

Burmese uses the Myanmar Unicode block. Words are not separated by spaces, so use chrF++ or a learned metric, not word BLEU.

Encoding is the main problem. Most legacy Burmese text uses Zawgyi, a non-standard encoding that stores letters in visual order. When the official switch to Unicode was planned, about 90% of device users were estimated to use Zawgyi. Zawgyi breaks search and translation; Facebook keeps conversion tools [2]. Before you translate or score Burmese text, detect Zawgyi and convert it to Unicode. Check that model output is Unicode.

We did not verify any Burmese-script OCR project.

## Data

- **Tipitaka in Myanmar script** (DatarrX): Pali Mula, Atthakatha and Tika, 462,504 paragraphs in JSONL, MIT license, from Pndaza's database [8]. A full Burmese Tipitaka translation is already in the Directory.
- **Asian Language Treebank (ALT)**: about 20,000 English news sentences translated into Burmese and 11 other languages; CC BY 4.0 [9].
- **myXNLI** (2025): a Burmese language inference test set, crowd-sourced and checked by experts; license not stated [10].
- **WMT26 Chinese–Southeast Asian task** (2026): aligned Chinese–Burmese data and a blind test set [11].

## Speech

Omnilingual ASR (Meta, November 2025) has a Burmese character error rate of 4.4, with 321.1 hours of training data [6]. Test sets differ between languages, so do not compare languages with this number. We found no Burmese Buddhist speech dataset.

## Machine translation

**BURMESE-SAN** (AI Singapore, NUS, KMITL; 2026) has 3,920 Burmese items, including 1,700 translation items, under CC BY-SA 4.0 [7]. Translation is scored on a MetricX-based scale (higher is better):

| System | Translation score | Overall | Year |
| --- | --- | --- | --- |
| Gemini 2.5 Pro | 90.22 | 72.35% | 2026 [7] |
| ERNIE 4.5 300B (best open-weight) | 86.25 | 54.68% | 2026 [7] |

Fine-tuning the Llama-based SEA-LION model on Southeast Asian data gave +19.29% in translation [7].

**Older benchmarks (FLORES-200, English → Burmese).**

| System | Metric | Score | Year |
| --- | --- | --- | --- |
| Google Translate | chrF++ | 40.4 | 2023 [12] |
| NLLB-200 (MoE) | chrF++ | 32.0 | 2023 [12] |
| ChatGPT (gpt-3.5), 5-shot | chrF++ | 20.6 | 2023 [12] |
| SeaLLMs 3 (7B) | chrF | 21.54 | 2024 [13] |

The 2023 results are old and do not show what newer models can do. chrF++ and BLEU numbers can only be compared between systems in the same language and direction, not between languages. No published test uses Buddhist text in Burmese.

### Shan and Mon

Shan is a Tai language written in the Myanmar script (code `shn`). Google Translate added Shan in its 2024 expansion of 110 languages; ModernMT, Baidu and Alibaba also offer Shan [14][15]. We did not find a Shan speaker count or any Shan translation benchmark. Mon is not in Google's 2024 list [14]. We found no Mon translation system, speaker count or NLP project.

## AI projects

- **BURMESE-SAN** benchmark (AI Singapore, NUS, KMITL) [7].
- Regional models that cover Burmese: Gemma-SEA-LION-v4-27B-IT (AI Singapore, August 2025) [16], Sailor2 (Sea AI Lab, Apache-2.0) [17], SeaLLMs 3 [13].
- We found no Burmese Buddhist AI project.

## Recommendation

To translate into Burmese today, use Gemini 2.5 Pro or a newer Gemini model with a Buddhist glossary. Check that input and output are Unicode, not Zawgyi. Have a native reviewer with Pali or monastic training check doctrinal terms. For Shan, Google Translate or Gemini may work, but there is no test (low confidence). For Mon we found no supported system.

Confidence: **medium**. BURMESE-SAN is a direct 2026 test with many translation items, so the evidence for general text is strong. But it does not use Buddhist text.

First test: take 50 to 100 sentences that have a trusted Burmese translation (for example from the Burmese Tipitaka translation in the Directory). Translate them with Gemini, one other frontier model and Google Translate. Score with chrF++ after Unicode normalization, and ask a reviewer to check Pali-derived terms.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Burmese, Shan, Mon. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (1)

- [Gemma-SEA-LION-v4-27B-IT](https://huggingface.co/aisingapore/Gemma-SEA-LION-v4-27B-IT) (AI Singapore): Gemma 3 based 27B chat model for Southeast Asian languages, including Burmese, Khmer, Lao, Thai and Vietnamese. Not Buddhist-specific.

**Datasets** (3)

- [Myanmar Tipitaka translation](https://huggingface.co/datasets/freococo/tipitaka_myanmar_translation_books) (freococo (community)): Burmese translation of the Tipitaka with the main commentaries and the Visuddhimagga, as JSONL.
- [Tipitaka in Myanmar script (DatarrX)](https://huggingface.co/datasets/DatarrX/tipitaka-dataset) (DatarrX (community)): Pali Mula, Atthakatha and Tika texts in Myanmar script, about 463,000 paragraphs as JSON.
- [Asian Language Treebank (ALT)](https://huggingface.co/datasets/alt) (NICT and partners): About 20,000 English Wikinews sentences translated into 12 Asian languages, including Thai, Lao, Khmer and Burmese. Not Buddhist-specific.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: Burmese language](https://en.wikipedia.org/wiki/Burmese_language), read 2026-11-17
2. [Frontier Myanmar: Zawgyi to Unicode, the big switch](https://www.frontiermyanmar.net/en/zawgyi-to-unicode-the-big-switch), read 2026-11-17
3. [Google Cloud Translation: language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
4. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
5. [openai/whisper tokenizer.py (language list)](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
6. [Omnilingual ASR per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
7. [BURMESE-SAN, arXiv 2602.18788](https://arxiv.org/html/2602.18788), read 2026-11-17
8. [DatarrX/tipitaka-dataset card](https://huggingface.co/datasets/DatarrX/tipitaka-dataset/blob/main/README.md), read 2026-11-17
9. [Asian Language Treebank dataset card](https://huggingface.co/datasets/alt/blob/main/README.md), read 2026-11-17
10. [myXNLI, arXiv 2504.09645](https://arxiv.org/abs/2504.09645v1), read 2026-11-17
11. [WMT26 Chinese–Southeast Asian shared task, ACL Anthology](https://aclanthology.org/2026.wmt-main.55/), read 2026-11-17
12. [Robinson et al. 2023, ChatGPT MT, arXiv 2309.07423, Table 11](https://arxiv.org/pdf/2309.07423), read 2026-11-17
13. [SeaLLMs 3, arXiv 2407.19672](https://arxiv.org/html/2407.19672v1), read 2026-11-17
14. [Google Translate Help: more than 100 new languages](https://support.google.com/translate/answer/15139004), read 2026-11-17
15. [machinetranslate.org: Shan](https://machinetranslate.org/shan), read 2026-11-17
16. [Gemma-SEA-LION-v4-27B-IT readme (mirror)](https://featherless.ai/models/aisingapore/Gemma-SEA-LION-v4-27B-IT/readme), read 2026-11-17
17. [Sea AI Lab: Sailor2](https://sail.sea.com/blog/articles/55), read 2026-11-17
