---
id: japanese
title: Japanese
kind: modern
group: Japanese, Korean, Vietnamese
countries: [Japan]
scripts: [Kanji, Hiragana, Katakana]
speakers: about 126 million (Ethnologue 2026)
directory_names: [Japanese]
resource_level: high
google_translate: yes (Translation LLM and NMT)
recommendation: Frontier LLM with a Buddhist glossary and native review
confidence: medium
updated: 2026-11
contributors: []
---

# Japanese

Japanese is the language of Japanese Buddhism and of a large body of Buddhist scholarship. Japanese Buddhists also read the Chinese canon as kanbun. Short answer: current AI models translate well into modern Japanese. For kanbun, they give the meaning but are weak at the traditional Japanese reading order.

## Summary

| | |
| --- | --- |
| Where | Japan and the diaspora |
| Speakers | about 126 million in total (Ethnologue 2026) [1] |
| Script | Kanji, hiragana, katakana |
| AI resources | high |
| Google Translate | yes, Translation LLM and NMT [2] |
| Microsoft Translator | yes, with LLM translation [3] |
| Speech to text | yes; Whisper large-v3 WER 4.8 on FLEURS [10] |
| Best evidence on translation quality | WMT24 human evaluation (2024) [7]; WMT25 automatic ranking (2025) [8] |

## Writing and text input

Unicode, fonts and input are mature. Japanese has no spaces between words.

OCR for premodern Japanese books is mature. NDL Kotenseki OCR (National Diet Library, v3.0) reaches about 92% average accuracy, as reported by its developers. It is called open source, but the license was not named. Its errors often look plausible, so they are hard to catch. Kanbun with reading marks was not discussed [13]. Google Research published "miwo", a kuzushiji recognition app [14]. SAT added 329 Taishō characters to Unicode 13.0 in 2020 [15].

## Data

- **SAT Daizōkyō Text Database** (University of Tokyo): Taishō canon text, images, and links to the DDB dictionary and BDK translations. Public use is approved by Daizō Shuppan, but no open license is named [15].
- CBETA also publishes the Taishō text. CBETA uses CC BY-NC-SA 4.0 with extra conditions. This limits commercial model training [20].
- **Kanbun data**: Kanbun-LM has 465 Tang poems with kundoku readings and translations [16]. KanbunKundoku has 9,292 sentences [17]. Neither is Buddhist, and neither states a license.
- We found no open Buddhist parallel set (for example Taishō to Japanese kakikudashi).

## Speech

- Whisper supports Japanese [12].
- **Benchmark**: Whisper large-v3 word error rate (WER, lower is better) is 4.8 on FLEURS and 15.2 on Common Voice 17 (2025 study) [10].
- Omnilingual ASR (2025) reports CER 19.2 for Japanese [11]. Character error rates for Japanese cannot be compared with other scripts.
- We found no dataset of Buddhist chanting or Dharma talks in Japanese.

## Machine translation

**Benchmark, WMT24, English to Japanese, human scores (higher is better), 2024** [7]: human reference 91.8; ONLINE-B 91.1; CommandR-plus 91.0; Claude-3.5-Sonnet 90.8; GPT-4 90.8; Gemini-1.5-Pro 90.0.

**Benchmark, WMT25 preliminary automatic ranking, English to Japanese (lower is better), 2025** [8]: Shy-hunyuan-MT 1.0, In2x 2.3, Gemini-2.5-Pro 2.4, GPT-4.1 2.9, DeepSeek-V3 4.6, Claude-4 5.7. Human evaluation replaces these.

**Benchmark, FLORES-200, English to Japanese, chrF++ (higher is better)**: NLLB about 25.2 [4]; in 2023, ChatGPT 5-shot 33.7 and Google Translate 37.1 [5]. These scores are low partly because chrF++ counts characters. chrF++ cannot be compared across languages.

**Vendor claim**: Claude models score 97.4–99.5% of their English score on Global-MMLU in Japanese. This tests knowledge, not translation [6].

All results are general text. We found no Buddhist test into Japanese. Older results may not show what current models can do.

## Classical form: kanbun

Kanbun is Classical Chinese read in Japanese order with marks (kundoku).

- **Benchmark (small, 50 sentences, 2025)**: Gemini-2.5-pro had the best BLEU (67.47), but its reading order was weak (PMR 76.39). GPT-5 had PMR 57.75. A fine-tuned model reached PMR 89.76. The authors say LLMs do not handle the reading marks well. Claude was not tested [17].
- Extra Classical Chinese training data helped kanbun and Korean hanja tasks very little [18].

## AI projects

- **BuddhaBot Plus and Buddharoid** (Kyoto University, Prof. Seiji Kumagai, with Teraverse Inc.): a Buddhist chatbot that uses ChatGPT, and a humanoid robot shown at Shoren-in in February 2026. Not for sale [19].
- **Swallow leaderboard** (Institute of Science Tokyo) added English–Japanese translation tests in 2026 [9].

## Recommendation

- **Into Japanese**: use a current frontier model (Gemini, GPT or Claude). Benchmarks show only small gaps between them. Always use a Buddhist glossary and a native reviewer.
- **From kanbun**: use an LLM for the meaning. Use a specialist or a fine-tuned model for the kundoku reading order.
- **Confidence: medium.** The evidence is general text, not Buddhist text.
- **First test**: take about 30 Buddhist passages with existing Japanese translations. Compare 3 models. Ask a native reviewer to mark term errors.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Japanese. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (2)

- [NDL Kotenseki OCR](https://github.com/ndl-lab/ndlkotenocr_cli) (National Diet Library (Japan)): OCR for digitized pre-modern Japanese and Chinese books (version 3), run with Docker.
- [BuddhaBot-Plus](https://www.kyoto-u.ac.jp/en/news/2025-03-03) (Kyoto University): Chatbot based on Buddhist scriptures, built on ChatGPT. Used with monks and nuns in Bhutan, and in Buddharoid, a humanoid robot monk made with Teraverse Inc. and shown at Shoren-in temple in Kyoto (not for sale).

**Datasets** (2)

- [KanbunKundoku](https://github.com/shiryusann/KanbunKundoku) (Zilong Li and Jie Cao): Classical Chinese sentences with kundoku reading marks and Japanese readings, for studying translation of Classical Chinese into Japanese.
- [Buddhist Philosophy Graph](https://huggingface.co/datasets/joyboseroy/buddhist-philosophy-graph) (joyboseroy (community)): Knowledge graph of nine Buddhist schools, from Theravada to Tibetan Vajrayana. Every link cites a named text with a quote.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: List of languages by total number of speakers (Ethnologue 2026)](https://en.wikipedia.org/wiki/Languages_by_total_speakers), read 2026-11-17
2. [Google Cloud Translation: Language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
3. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
4. [NLLB metrics, public copy (Mara4444/MSc_Thesis)](https://raw.githubusercontent.com/Mara4444/MSc_Thesis/main/datasets/others/nllb_metrics.csv), read 2026-11-17
5. [Robinson et al. 2023, ChatGPT MT, arXiv 2309.07423](https://arxiv.org/pdf/2309.07423), read 2026-11-17
6. [Claude docs: Multilingual support](https://platform.claude.com/docs/en/build-with-claude/multilingual-support), read 2026-11-17
7. [WMT24 Findings](https://aclanthology.org/2024.wmt-1.1.pdf), read 2026-11-17
8. [WMT25 preliminary ranking, arXiv 2508.14909](https://arxiv.org/html/2508.14909v2), read 2026-11-17
9. [Swallow leaderboard, about page](https://swallow-llm.github.io/leaderboard/about.en.html), read 2026-11-17
10. [Dolphin paper, arXiv 2503.20212](https://arxiv.org/pdf/2503.20212), read 2026-11-17
11. [Omnilingual ASR per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
12. [openai/whisper tokenizer.py](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
13. [Digital Orientalist: Overview of NDL Kotenseki OCR, 2026-02-24](https://digitalorientalist.com/2026/02/24/overview-of-ndl%E5%8F%A4%E5%85%B8%E7%B1%8Docr-the-key-to-early-modern-japanese-archives), read 2026-11-17
14. [Google Research: miwo](https://research.google/pubs/miwo-ai-kuzushiji-recognition-application-for-document-examination/), read 2026-11-17
15. [SAT Daizōkyō Text Database](https://21dzk.l.u-tokyo.ac.jp/SAT/index_en.html), read 2026-11-17
16. [Kanbun-LM, arXiv 2305.12759](https://arxiv.org/pdf/2305.12759), read 2026-11-17
17. [Li and Cao, KanbunKundoku, arXiv 2511.05239](https://arxiv.org/html/2511.05239v1), read 2026-11-17
18. [Song et al., arXiv 2411.04822](https://arxiv.org/abs/2411.04822), read 2026-11-17
19. [Adnkronos/Jiji: Japanese group develops Buddhist AI humanoid robot, 2026-06-25](https://english.adnkronos.com/2026/06/25/focus-japanese-group-develops-buddhist-ai-humanoid-robot/), read 2026-11-17
20. [CBETA Copyright Notice](https://cbeta.org/en/copyright), read 2026-11-17
