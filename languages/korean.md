---
id: korean
title: Korean
kind: modern
group: Japanese, Korean, Vietnamese
countries: [South Korea, North Korea]
scripts: [Hangul, Hanja]
speakers: about 82 million (Ethnologue 2026)
directory_names: [Korean]
resource_level: high
google_translate: yes (Translation LLM and NMT)
recommendation: Frontier LLM with a Buddhist glossary and native review
confidence: medium
updated: 2026-11
contributors: []
---

# Korean

Korean is the language of Korean Buddhism, including the Jogye Order. Korean Buddhists also read the Chinese canon as hanmun, and the Tripitaka Koreana woodblocks are kept at Haeinsa. Short answer: current AI models translate well into modern Korean. For hanmun, specialized models and existing Korean translations help.

## Summary

| | |
| --- | --- |
| Where | South Korea, North Korea and the diaspora |
| Speakers | about 82 million in total (Ethnologue 2026) [1] |
| Script | Hangul; Hanja (Chinese characters) in older and specialist texts |
| AI resources | high |
| Google Translate | yes, Translation LLM and NMT [2] |
| Microsoft Translator | yes, with LLM translation [3] |
| Speech to text | yes; Whisper large-v3 WER 2.6 on FLEURS [7] |
| Best evidence on translation quality | WMT25 automatic ranking (2025) [6] |

## Writing and text input

Unicode, fonts and input for Hangul are mature. Older Buddhist texts use Hanja or mixed Hanja and Hangul. We did not verify how many Korean Hanja variants are in Unicode.

The Tripitaka Koreana has research OCR data with page images and character labels (TKH/MTH) [10]. In 2024 the Cultural Heritage Administration announced a digital database of the Haeinsa woodblocks: photographs of each block and a public web service, to be developed from 2025 [11]. We did not verify whether the service is live.

## Data

- **Open Korean Historical Corpus** (2025): 18 million documents, 5 billion tokens, 7th century to 2025, including Idu and mixed Hanja–Hangul text. License CC BY 4.0 [12].
- **ITKC database**: Korean classics in hanmun with Korean translations [13].
- **Korea Archives of Buddhist Culture** (Academy of Buddhist Studies, Dongguk University): reviewed in 2023. We did not verify its contents or size [17].
- A 2025 paper says Korean Buddhist documentary heritage is mostly kept in archives and not yet in active use [18].
- Chinese canon text from CBETA uses CC BY-NC-SA 4.0 with extra conditions. This limits commercial model training [19].
- We did not verify the online status or license of the Dongguk Hangul Tripitaka.

## Speech

- Whisper supports Korean [9]. The Whisper paper says Korean does worse than its training data size predicts [20].
- **Benchmark**: Whisper large-v3 word error rate (lower is better) is 2.6 on FLEURS and 11.9 on Common Voice 17 (2025 study) [7].
- Omnilingual ASR (2025) reports CER 5.8 for Korean [8].
- We found no dataset of Buddhist chanting or Dharma talks in Korean.

## Machine translation

**Benchmark, WMT25 preliminary automatic ranking, English to Korean (lower is better), 2025** [6]: Shy-hunyuan-MT 1.0, Gemini-2.5-Pro 2.5, GPT-4.1 2.8, Claude-4 4.3, DeepSeek-V3 5.0. Human evaluation replaces these.

**Benchmark, FLORES-200, English to Korean, chrF++ (higher is better)**: NLLB about 34.3 [4]; in 2023, ChatGPT 5-shot 34.9 and Google Translate 38.6 [5]. chrF++ cannot be compared across languages.

**Vendor claim**: Claude models score 97.0–99.6% of their English score on Global-MMLU in Korean. This tests knowledge, not translation [21].

All results are general text. We found no Buddhist test into Korean. Older results may not show what current models can do.

## Classical form: hanmun

Hanmun is Classical Chinese as written and read in Korea.

- **Benchmark (H2KE, 2022–2023)**: a specialized model translating Hanja historical records reached BLEU about 46.1 into modern Korean, against 11.10 for Papago. Into English: about 24.6 against 3.59. It was trained on the Annals of Joseon, about 360,000 Hanja–Korean pairs [13]. This is not Buddhist text.
- Extra Classical Chinese training data helped hanja tasks very little (at most +0.84 BLEU) [14].

## AI projects

- **ETRI** announced in 2023 an AI platform to translate old documents in Chinese characters. Buddhist texts are not mentioned [15].
- A Jogye Order Monastic College seminar at Dongguk University in 2025 discussed AI and presented Dharmamitra and CBETA search [16].

## Recommendation

- **Into Korean**: use a current frontier model (Gemini, GPT or Claude). Benchmarks show only small gaps. Use a glossary of Sino-Korean Buddhist terms and a native reviewer.
- **From hanmun**: use an LLM, and check against ITKC or other existing Korean translations. Specialized models did much better than Papago on historical Hanja.
- **Confidence: medium.** The evidence is general text, not Buddhist text.
- **First test**: take about 30 Buddhist passages with existing Korean translations. Compare 3 models. Ask a native reviewer to mark term errors.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Korean. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (0)

None listed yet.

**Datasets** (0)

None listed yet.

<!-- in-directory:end -->

## Sources

1. [Wikipedia: List of languages by total number of speakers (Ethnologue 2026)](https://en.wikipedia.org/wiki/Languages_by_total_speakers), read 2026-11-17
2. [Google Cloud Translation: Language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
3. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
4. [NLLB metrics, public copy (Mara4444/MSc_Thesis)](https://raw.githubusercontent.com/Mara4444/MSc_Thesis/main/datasets/others/nllb_metrics.csv), read 2026-11-17
5. [Robinson et al. 2023, ChatGPT MT, arXiv 2309.07423](https://arxiv.org/pdf/2309.07423), read 2026-11-17
6. [WMT25 preliminary ranking, arXiv 2508.14909](https://arxiv.org/html/2508.14909v2), read 2026-11-17
7. [Dolphin paper, arXiv 2503.20212](https://arxiv.org/pdf/2503.20212), read 2026-11-17
8. [Omnilingual ASR per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
9. [openai/whisper tokenizer.py](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
10. [TKH/MTH datasets (HCIILAB)](https://github.com/HCIILAB/TKH_MTH_Datasets_Release), read 2026-11-17
11. [Asia Economy: Tripitaka Koreana digital database, 2024-03-18](https://www.asiae.co.kr/en/article/2024031809334052844), read 2026-11-17
12. [Open Korean Historical Corpus, arXiv 2510.24541 (paper page)](https://fugumt.com/fugumt/paper_check/2510.24541v1_enmode), read 2026-11-17
13. [Son et al., Translating Hanja Historical Documents, arXiv 2205.10019](https://arxiv.org/html/2205.10019v5), read 2026-11-17
14. [Song et al., arXiv 2411.04822](https://arxiv.org/abs/2411.04822), read 2026-11-17
15. [Daum news: ETRI old-document translation platform, 2023-09-21](https://v.daum.net/v/20230921142401572), read 2026-11-17
16. [Korea Times, 2025-10-24](https://www.koreatimes.co.kr/amp/lifestyle/trends/20251024/will-ai-replace-spiritual-practice-priests-and-monks-join-the-ai-age), read 2026-11-17
17. [Review of the Korea Archives of Buddhist Culture, The Review of Korean Studies 26(2)](https://accesson.kr/rks/v.26/2/236/33903), read 2026-11-17
18. [Park and Seo, Namdo Culture Studies 54, 2025](https://www.earticle.net/Article/A466801), read 2026-11-17
19. [CBETA Copyright Notice](https://cbeta.org/en/copyright), read 2026-11-17
20. [Radford et al. 2022, Whisper, arXiv 2212.04356](https://arxiv.org/pdf/2212.04356), read 2026-11-17
21. [Claude docs: Multilingual support](https://platform.claude.com/docs/en/build-with-claude/multilingual-support), read 2026-11-17
