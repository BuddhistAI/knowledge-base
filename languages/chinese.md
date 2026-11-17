---
id: chinese
title: Chinese
kind: modern
group: Chinese
countries: [China, Taiwan, Hong Kong, Singapore, Malaysia]
scripts: [Simplified Chinese, Traditional Chinese]
speakers: Mandarin about 1.18 billion and Cantonese about 86 million (Ethnologue 2026)
speakers_n: 1264000000
speakers_year: 2022 and 2023
speakers_source: https://en.wikipedia.org/wiki/Mandarin_Chinese
speakers_basis: Mandarin and Cantonese added together
directory_names: [Chinese, Cantonese]
resource_level: high
google_translate: yes (Simplified and Traditional; Cantonese NMT only)
recommendation: Frontier LLM with a Buddhist glossary and native review
confidence: medium
updated: 2026-11
contributors: []
---

# Chinese

Modern Chinese is used by Buddhists in mainland China, Taiwan, Hong Kong, Singapore, Malaysia and the diaspora. This page covers Mandarin (simplified and traditional characters), Cantonese, and briefly Hokkien. For the canon, see [Classical Chinese](classical-chinese.md). Short answer: current AI models write fluent Chinese. Buddhist terms still need review.

## Summary

| | |
| --- | --- |
| Where | China, Taiwan, Hong Kong, Singapore, Malaysia |
| Speakers | Mandarin about 1,183 million in total; Cantonese (Yue) about 86 million (Ethnologue 2026) [1] |
| Script | Simplified and Traditional Chinese characters |
| AI resources | high |
| Google Translate | Simplified and Traditional: LLM and NMT. Cantonese: NMT only [2] |
| Microsoft Translator | Simplified, Traditional and Cantonese; LLM translation for Simplified and Traditional [3] |
| Speech to text | Whisper and Omnilingual ASR support Mandarin and Cantonese [7][8] |
| Best evidence on translation quality | WMT24 human evaluation (2024) [6]; per-pair results not read |

## Writing and text input

Mandarin is written in simplified characters (mainland China, Singapore, Malaysia) and traditional characters (Taiwan, Hong Kong). Text input and Unicode support are mature. The Buddhist canon and Taiwanese Buddhist institutions use traditional characters. Output for Taiwan or Hong Kong should follow local conventions. Simple conversion from simplified text is not enough. This is our advice, not a test result.

Hokkien (Min Nan): we did not find a verified speaker figure. It is not in the Ethnologue table we used [1]. We have no verified data on AI support for Hokkien.

## Data

General Chinese text is very large. We did not research general web corpora in depth.

For Buddhist text, the main source is CBETA, in Classical Chinese. Its license is CC BY-NC-SA 4.0 with extra conditions: no commercial use, and the core content must stay unchanged. This matters for model training [10]. We found no open Buddhist parallel set from Classical Chinese into modern Chinese. Published Dharma talk archives exist at large Taiwanese organizations, but we did not verify their rights.

## Speech

- Whisper supports Chinese and Cantonese [7]. The Whisper paper says Chinese does worse than its training data size predicts [14].
- Meta Omnilingual ASR (7B, 2025) reports character error rate (CER, lower is better): Mandarin simplified 11.5, Mandarin traditional 11.8, Cantonese 17.0 [8]. Each language has its own test set, so these numbers are not a ranking.
- We found no Buddhist speech dataset in Chinese.

## Machine translation

**Benchmark: FLORES-200, English to Chinese, chrF++ (higher is better).**

| System (year) | Simplified | Traditional | Cantonese |
| --- | --- | --- | --- |
| NLLB-200, probably 3.3B (2022) [4] | 22.3 | 14.4 | 15.5 |
| NLLB-MoE (2023 study) [5] | 22.8 | 14.0 | 17.9 |
| ChatGPT gpt-3.5, 5-shot (2023) [5] | 31.9 | 26.0 | 27.2 |
| Google Translate (2023) [5] | 37.8 | not reported | not reported |

These scores are low partly because chrF++ counts characters, and Chinese has no spaces and many distinct characters. chrF++ numbers cannot be compared across languages. They can only compare systems on the same language. The NLLB values come from a copy of the official file; which model it is was not verified [4]. These results are from 2022–2023 and do not show what current models can do.

**Benchmark: WMT24**, with expert human ratings, tested 8 LLMs and 4 online systems. Its conclusion: "The LLM Era Is Here but MT Is Not Solved Yet" [6]. We did not read the English-to-Chinese ranking.

**Vendor claim**: Anthropic reports that Claude models score 97.7–99.6% of their English score on Global-MMLU in Simplified Chinese. This tests knowledge, not translation [9].

We found no test of Buddhist translation into modern Chinese.

## AI projects

- **Breeze 2** (MediaTek Research, 2025): Traditional Chinese LLMs, 3B and 8B, Llama 3.2 license [11].
- **TAIDE** (Taiwan national project): Traditional Chinese models on Hugging Face [12].
- **CBETA AI semantic search** (DILA, 2025): Chinese search with AI summaries over the canon [13].
- **Xian'er** robot monk (Longquan Monastery, Beijing): in 2018 it planned an AI upgrade with iFlytek and Tencent. We found no newer technical source [15].

## Recommendation

- **Into Chinese**: use a current frontier model (for example Claude, GPT, Gemini, DeepSeek or Qwen). Give it a Buddhist glossary and ask a native Buddhist reader to review. For traditional output, ask for Taiwan or Hong Kong usage in the prompt. Cantonese and Hokkien text output is a low priority, because Buddhist publishing mostly uses standard written Chinese. This is an inference.
- **Confidence: medium.** Fluency is well supported. Accuracy of Buddhist terms is not tested.
- **First test**: take about 30 English Buddhist passages with known key terms. Translate them with 3 models into simplified and traditional Chinese. Ask a native reviewer to mark term errors and fluency.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Chinese, Cantonese. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (7)

- [Buddhist AI Translator (慧译通)](https://github.com/xr843/Buddhist-AI-Translator) (xr843 (community)): AI translator for Buddhist texts with support for Sanskrit, Pali and Tibetan terms.
- [BDRC - Buddhist Digital Resource Center](https://www.bdrc.io/) (BDRC): The largest digital library of Tibetan texts (scans, e-texts and catalog). In 2026 it started an initiative to build open Buddhist datasets for AI, and it publishes OCR models and datasets on Hugging Face.
- [SuttaCentral](https://suttacentral.net/) (SuttaCentral): Early Buddhist texts with parallels across languages and many translations. Texts and parallels are on GitHub (sc-data).
- [CBETA semantic search (CBSS)](https://cbetaonline.dila.edu.tw/cbss/) (Dharma Drum Institute of Liberal Arts and CBETA): Ask questions in plain language and get matching passages from the CBETA canon, with AI summaries of the top passages (built on the OpenAI API).
- [Xunzi models for Chinese classics](https://github.com/Xunzi-LLM-of-Chinese-classics/XunziALLM) (Nanjing Agricultural University with Zhonghua Book Company): Open models (Qwen, Baichuan2 and ChatGLM3 based) for ancient Chinese texts: translation into modern Chinese, punctuation, word segmentation and entity extraction.
- [Master-skill](https://github.com/xr843/Master-skill) (xr843 (community)): Framework for Buddhist AI personas that answer from sources (using FoJin) and know their limits.
- [awesome-buddhist-dharma](https://github.com/yuqianyi1001/awesome-buddhist-dharma) (yuqianyi1001 (community)): Collection of Buddhist study resources, mostly in Chinese.

**Datasets** (5)

- [BK-EVAL (佛典知識評測資料集)](https://github.com/DILA-edu/BK-EVAL) (Dharma Drum Institute of Liberal Arts): Evaluation set on knowledge of the Chinese Buddhist canon.
- [WYWEB](https://github.com/baudzhou/WYWEB) (baudzhou (ACL Findings 2023 authors)): Nine Classical Chinese tasks, including punctuation, named entities and translation into modern Chinese (about 26,000 pairs). Part of the punctuation data comes from Buddhist scriptures.
- [SuttaCentral data (sc-data)](https://github.com/suttacentral/sc-data) (SuttaCentral): Texts, translations and parallels behind SuttaCentral.
- [Buddhist Philosophy Graph](https://huggingface.co/datasets/joyboseroy/buddhist-philosophy-graph) (joyboseroy (community)): Knowledge graph of nine Buddhist schools, from Theravada to Tibetan Vajrayana. Every link cites a named text with a quote.
- [Buddhist LLM fine-tuning data](https://github.com/guyiicn/buddhist-llm-finetune) (guyiicn (community)): 4,386 question and answer pairs on 18 CBETA scriptures, with fine-tuning scripts.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: List of languages by total number of speakers (Ethnologue 2026)](https://en.wikipedia.org/wiki/Languages_by_total_speakers), read 2026-11-17
2. [Google Cloud Translation: Language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
3. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
4. [NLLB metrics, public copy (Mara4444/MSc_Thesis)](https://raw.githubusercontent.com/Mara4444/MSc_Thesis/main/datasets/others/nllb_metrics.csv), read 2026-11-17
5. [Robinson et al. 2023, ChatGPT MT, arXiv 2309.07423](https://arxiv.org/pdf/2309.07423), read 2026-11-17
6. [WMT24 Findings](https://dare.uva.nl/id/de0ad3be-830a-4a35-a71b-d946c07764de), read 2026-11-17
7. [openai/whisper tokenizer.py](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
8. [Omnilingual ASR per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
9. [Claude docs: Multilingual support](https://platform.claude.com/docs/en/build-with-claude/multilingual-support), read 2026-11-17
10. [CBETA Copyright Notice](https://cbeta.org/en/copyright), read 2026-11-17
11. [Breeze 2, arXiv 2501.13921](https://arxiv.org/abs/2501.13921), read 2026-11-17
12. [TAIDE on Hugging Face](https://huggingface.co/taide), read 2026-11-17
13. [CBETA x AI semantic search demo page](https://cbeta.org/?p=28688), read 2026-11-17
14. [Radford et al. 2022, Whisper, arXiv 2212.04356](https://arxiv.org/pdf/2212.04356), read 2026-11-17
15. [Buddhistdoor: China's robot monk to receive an AI upgrade, 2018-05-15](https://www2.buddhistdoor.net/news/chinas-robot-monk-to-receive-an-ai-upgrade), read 2026-11-17
