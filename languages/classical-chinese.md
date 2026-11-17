---
id: classical-chinese
title: Classical Chinese
kind: classical
group: Chinese
countries: [China, Taiwan, Hong Kong, Japan, South Korea, Vietnam]
scripts: [Chinese characters (traditional)]
speakers: not verified (a written language with no native speakers)
directory_names: [Classical Chinese]
resource_level: medium
google_translate: not verified
recommendation: Frontier LLM with RAG over CBETA and DDB; compare with MITRA
confidence: low
updated: 2026-11
contributors: []
---

# Classical Chinese

Classical Chinese is the language of the Chinese Buddhist canon. People also read it in Japan (kanbun), Korea (hanmun) and Vietnam (Hán). The canon is fully digital. AI can translate it, but there is no recent test of current models on Buddhist texts.

## Summary

| | |
| --- | --- |
| Where | Chinese, Japanese, Korean and Vietnamese Buddhism |
| Speakers | No native speakers; read by monastics and scholars |
| Script | Traditional Chinese characters |
| AI resources | medium |
| Google Translate | not verified |
| Microsoft Translator | not verified |
| Speech to text | Not applicable; no chanting dataset found |
| Best evidence on translation quality | MITRA-zh-eval, Buddhist Chinese to English (2025) [11] |

## Writing and text input

The canon uses traditional characters. CBETA uses its own system for rare characters that are not in Unicode. We did not verify how many of these are now in Unicode.

OCR for premodern Chinese works at scale. The Chinese Text Project ran automatic OCR on over 25 million pages, with crowd correction. No accuracy figure is given [3]. In 2025 CBETA started to use AI for OCR and for modern punctuation. AI makes a draft and humans review it [1]. Page images with character labels exist for the Tripitaka Koreana and other canons (TKH/MTH) [17].

## Data

- **CBETA**: by the end of 2025, 4,868 texts, 21,955 fascicles and over 220 million characters [1].
- **License**: CBETA uses CC BY-NC-SA 4.0 with extra conditions. Use must be non-commercial, and the core content must stay unchanged. Some collections (for example Yin Shun, Lü Cheng, Taixu and Yanpei) are not under Creative Commons [2]. This matters for model training: a model trained on CBETA and released for commercial use is a legal risk.
- **CBETA-txt**: plain text of Taishō vols. 1–55 and 85, with and without punctuation. License not stated [4].
- **Kanseki Repository**: premodern Chinese texts with a Buddhist section (KR6). Its server is down since 2026-02-05 [5].
- **SAT Daizōkyō** (Tokyo): Taishō text and images; public use is approved by Daizō Shuppan, but no open license is named [7].
- **Digital Dictionary of Buddhism (DDB)**: over 73,000 entries (2019); guests get 10 searches a day [6].
- **Parallel data**: MITRA-zh-eval has 2,662 Buddhist Chinese–English pairs from 32 texts [11]. The BDK English Tripiṭaka has free PDFs, but "All Rights Reserved" [10]. Classical-to-modern Chinese pairs exist in general (mostly not Buddhist) sets: WYWEB (20k train pairs) [8] and C3Bench (10k translation pairs) [9].

## Speech

Classical Chinese is read and chanted, not spoken. We found only archive recordings of chanting, not datasets for machine learning [18].

## Machine translation

All results below are **benchmarks** unless marked. Most are from 2023–2024 and may not show what newer models can do.

| Test | What it measures | Result | Year |
| --- | --- | --- | --- |
| ACLUE [12] | Ancient Chinese, multiple choice, accuracy (higher is better) | Best ChatGLM2 37.4%, ChatGPT 36.9%, random 25% | 2023 |
| WenMind [13] | Ancient to modern Chinese translation score (higher is better) | Qwen1.5-72B-Chat 64.6, Xunzi-Qwen1.5-7B 63.4, ERNIE-4.0 62.8 | 2024 |
| C3Bench [9] | Classical to modern Chinese, BLEU (higher is better) | Best LLM 34.58 (Spark-v3); supervised methods were better | 2024 |
| MITRA-zh-eval [11] | Buddhist Chinese to English; GEMBA and 5 expert raters | Domain-trained open models competitive with GPT-4 Turbo, Claude 3.5, Gemini; RAG helped the best commercial models | 2025 |

MITRA-zh-eval found that GEMBA, a metric that uses an LLM as judge, agreed best with the experts [11]. The paper does not name one top model. The newest MITRA model (mitra-qwen35-it, 9B, Apache-2.0, trained July 2026) covers Buddhist Chinese, but its card has no scores [14]. We found no published test of GPT-5, Claude 4.x or newer, or Gemini 3 on Buddhist Classical Chinese. Any claim that one of them is best is **anecdotal**.

## AI projects

- **CBETA AI semantic search (CBSS)**, by DILA, public beta 2025: search in plain language over CBETA, with AI summaries. It uses the OpenAI API with RAG [16].
- **Xunzi** models (Nanjing Agricultural University with Zhonghua Book Company, 2023): open models that translate ancient texts into modern Chinese. They are not Buddhist-specific [15].
- **MITRA / Dharmamitra**: Buddhist translation models and data [11][14].

## Recommendation

- **From Classical Chinese** (into English or modern languages): use a current frontier model with retrieval (RAG) over CBETA and DDB glossaries. Compare it with the MITRA model on the same passages. Have a specialist review the output.
- **Into Classical Chinese**: this is rarely needed. We found no evidence on it.
- **Confidence: low.** The Buddhist test (2025) used older models. No test of 2025–2026 frontier models exists.
- **First test**: run 3–5 current models, with and without RAG, on a sample of MITRA-zh-eval. Score with GEMBA and ask one specialist to rate about 50 outputs. Keep CBETA-derived data internal and non-commercial.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Classical Chinese. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (19)

- [Dharmamitra](https://dharmamitra.org/) (Dharmamitra team (UC Berkeley and partners)): Machine translation, grammar analysis and search for Buddhist source languages. Its MITRA models are published on Hugging Face.
- [Dharmamitra dictionaries and lexicon](https://github.com/dharmamitra/dharmamitra-stardict-dictionaries) (Dharmamitra team): StarDict dictionaries and a lexicon built from Dharmamitra's parallel text collection.
- [Digital Dictionary of Buddhism (DDB)](https://www.buddhism-dict.net/ddb/) (A. Charles Muller): Online dictionary of East Asian Buddhist terms, started in 1995. Visitors can search as "guest" with a limited number of searches per day.
- [CBETA](https://www.cbeta.org/) (Chinese Buddhist Electronic Text Association): Digital edition of the Chinese Buddhist canon, with an online reader (CBETA Online), XML files on GitHub and an API.
- [SAT Daizōkyō Text Database](https://21dzk.l.u-tokyo.ac.jp/SAT/) (University of Tokyo): Searchable Taishō edition of the Chinese Buddhist canon.
- [DILA Authority Databases](https://authority.dila.edu.tw/) (Dharma Drum Institute of Liberal Arts): Reference data on people, places, times and catalogs for Buddhist studies. Also on GitHub.
- [DharmaNexus](https://dharmanexus.org/) (Dharmamitra team (successor of BuddhaNexus)): Finds parallel and similar passages across the Pali, Sanskrit, Tibetan and Chinese canons.
- [FoJin](https://fojin.app/) (xr843 (community)): Buddhist text platform with more than 10,000 texts from over 600 sources and search across languages.
- [Deer Park](https://deerpark.app/) (deerpark.app): Reader for Chinese Buddhist texts. An agent skill lets AI agents look up and read texts through its public URLs.
- [CBETA semantic search (CBSS)](https://cbetaonline.dila.edu.tw/cbss/) (Dharma Drum Institute of Liberal Arts and CBETA): Ask questions in plain language and get matching passages from the CBETA canon, with AI summaries of the top passages (built on the OpenAI API).
- [Kanseki Repository (漢リポ)](https://kanripo.org/) (Kanseki Repository): Premodern Chinese texts kept as GitHub repositories, with a Buddhist section (KR6). The web server has been down since February 2026.
- [Kim Hán Nôm](https://kimhannom.fit.hcmus.edu.vn/) (University of Science, VNU-HCM (Center for Computational Linguistics)): OCR for printed and handwritten Hán and Nôm texts (Buddhist scripture is one document type), transliteration into Quốc ngữ and experimental translation. Web, mobile apps and API.
- [NDL Kotenseki OCR](https://github.com/ndl-lab/ndlkotenocr_cli) (National Diet Library (Japan)): OCR for digitized pre-modern Japanese and Chinese books (version 3), run with Docker.
- [MITRA models (buddhist-nlp)](https://huggingface.co/buddhist-nlp) (Dharmamitra team): About 60 models for Buddhist languages - translation (Gemma, Qwen, NLLB and mBART based), embeddings, sentence alignment, tagging and OCR.
- [Xunzi models for Chinese classics](https://github.com/Xunzi-LLM-of-Chinese-classics/XunziALLM) (Nanjing Agricultural University with Zhonghua Book Company): Open models (Qwen, Baichuan2 and ChatGLM3 based) for ancient Chinese texts: translation into modern Chinese, punctuation, word segmentation and entity extraction.
- [Dharmamitra Claude Code agent](https://github.com/dharmamitra/dharmamitra-claude-code-agent) (Dharmamitra team): Starter pack for agent-based translation, critical editions and finding parallel passages.
- [Deer Park skill](https://github.com/briansun/deerpark-skill) (briansun (community)): Agent skill to search and read Chinese Buddhist texts on deerpark.app.
- [buddhist-canons skill](https://github.com/luohy-qh/buddhist-canons) (luohy-qh (community)): Agent skill built from 19 canons (2,494 texts) as searchable evidence cards that keep the source text apart from AI summaries.
- [Chinese kepan outliner](https://github.com/aaronbao1/chinese-kepan-outliner) (aaronbao1 (community)): Claude skill that recovers the kēpàn (科判) outlines of classical Chinese Buddhist texts.

**Datasets** (13)

- [MITRA-zh-eval](https://aclanthology.org/2025.nlp4dh-1.12) (Dharmamitra team): 2,662 Classical Chinese to English sentence pairs from the Chinese canon for evaluating translation.
- [BK-EVAL (佛典知識評測資料集)](https://github.com/DILA-edu/BK-EVAL) (Dharma Drum Institute of Liberal Arts): Evaluation set on knowledge of the Chinese Buddhist canon.
- [WYWEB](https://github.com/baudzhou/WYWEB) (baudzhou (ACL Findings 2023 authors)): Nine Classical Chinese tasks, including punctuation, named entities and translation into modern Chinese (about 26,000 pairs). Part of the punctuation data comes from Buddhist scriptures.
- [CBETA XML P5](https://github.com/cbeta-org/xml-p5) (CBETA): The full Chinese Buddhist canon of CBETA in TEI XML.
- [CBETA Chinese canon (Hugging Face copy)](https://huggingface.co/datasets/linhgiang/cbeta-chinese-canon) (linhgiang (community)): The CBETA canon as a ready-to-use dataset.
- [Daizhige](https://huggingface.co/datasets/buddhist-nlp/daizhige) (Dharmamitra team): Large Classical Chinese corpus (Daizhige collection).
- [CBETA-txt](https://github.com/DILA-edu/CBETA-txt) (Dharma Drum Institute of Liberal Arts): Plain text of Taishō volumes 1-55 and 85, made from the CBETA XML, with and without punctuation.
- [MITRA parallel data](https://github.com/dharmamitra/mitra-parallel) (Dharmamitra team): Parallel sentence data from the Dharmamitra project.
- [Mitrasaṃgraha](https://huggingface.co/datasets/buddhist-nlp/mitrasamgraha-released-data-only) (Dharmamitra team): Released part of the Dharmamitra parallel data collection. The paper version on GitHub (dharmamitra/mitrasamgraha-dataset) has 391,548 Sanskrit-English pairs with a test set.
- [BDK English Tripiṭaka](https://bdk-seiten.com/translation.php?lang=en) (Bukkyō Dendō Kyōkai (BDK)): English translations of texts from the Taishō canon (139 works in the first stage), as free PDFs.
- [KanbunKundoku](https://github.com/shiryusann/KanbunKundoku) (Zilong Li and Jie Cao): Classical Chinese sentences with kundoku reading marks and Japanese readings, for studying translation of Classical Chinese into Japanese.
- [Tripitaka Koreana in Han (TKH, MTH)](https://github.com/HCIILAB/TKH_MTH_Datasets_Release) (HCIILAB): Page images of the Tripitaka Koreana and other Chinese canons with character annotation.
- [MITRA instruction data](https://huggingface.co/datasets/buddhist-nlp/mitra-instructions) (Dharmamitra team): Instruction data from the MITRA project.

<!-- in-directory:end -->

## Sources

1. [CBETA 2026 New Year announcement](https://cbeta.org/post/29961), read 2026-11-17
2. [CBETA Copyright Notice](https://cbeta.org/en/copyright), read 2026-11-17
3. [Sturgeon, Large-scale OCR of Pre-modern Chinese Texts](https://dsturgeon.net/large-scale-ocr-chinese/), read 2026-11-17
4. [DILA-edu/CBETA-txt on GitHub](https://github.com/DILA-edu/CBETA-txt), read 2026-11-17
5. [Kanseki Repository](https://kanripo.org/), read 2026-11-17
6. [Wikipedia: Digital Dictionary of Buddhism](https://en.wikipedia.org/wiki/Digital_Dictionary_of_Buddhism), read 2026-11-17
7. [SAT Daizōkyō Text Database](https://21dzk.l.u-tokyo.ac.jp/SAT/index_en.html), read 2026-11-17
8. [WYWEB, ACL Findings 2023](https://arxiv.org/pdf/2305.14150), read 2026-11-17
9. [C3Bench, arXiv 2405.17732](https://arxiv.org/html/2405.17732v2), read 2026-11-17
10. [BDK English Tripiṭaka](https://bdk-seiten.com/translation.php?lang=en), read 2026-11-17
11. [MITRA-zh-eval, ACL Anthology 2025.nlp4dh-1.12](https://aclanthology.org/2025.nlp4dh-1.12), read 2026-11-17
12. [ACLUE, arXiv 2310.09550](https://arxiv.org/html/2310.09550v1), read 2026-11-17
13. [WenMind, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c1019b5711474ae5627dc8580614e01-Paper-Datasets_and_Benchmarks_Track.pdf), read 2026-11-17
14. [buddhist-nlp/mitra-qwen35-it model card](https://huggingface.co/buddhist-nlp/mitra-qwen35-it), read 2026-11-17
15. [Xunzi LLM announcement, chinakongzi.org, 2023-12-14](https://chinakongzi.org/English/CulturalHighlights/202312/t20231214_569207.htm), read 2026-11-17
16. [CBETA x AI semantic search demo page](https://cbeta.org/?p=28688), read 2026-11-17
17. [TKH/MTH datasets (HCIILAB)](https://github.com/HCIILAB/TKH_MTH_Datasets_Release), read 2026-11-17
18. [CREM-CNRS archive: Chinese Buddhist chanting, 1969](https://archives.crem-cnrs.fr/archives/items/CNRSMH_E_1969_018_006_09/), read 2026-11-17
