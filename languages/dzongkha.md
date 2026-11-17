---
id: dzongkha
title: Dzongkha
kind: modern
group: Tibetic
countries: [Bhutan]
scripts: [Tibetan]
speakers: not verified
directory_names: [Dzongkha]
resource_level: low
google_translate: yes (since 2024)
recommendation: Google Translate as a baseline with native review
confidence: low
updated: 2026-11
contributors: []
---

# Dzongkha

Dzongkha is the national language of Bhutan [1]. AI support is new and small. Google Translate and a Bhutan government system can translate into Dzongkha, but there are no recent public quality scores.

## Summary

| | |
| --- | --- |
| Where | Bhutan |
| Speakers | not verified |
| Script | Tibetan script |
| AI resources | low |
| Google Translate | yes, added in June 2024 [2]; in the Cloud API as NMT only [3] |
| Microsoft Translator | no [4] |
| Speech to text | not in Whisper [8]; Meta Omnilingual ASR and a Bhutan MMS fine-tune [9] [1] |
| Best evidence on translation quality | FLORES-200, NLLB and ChatGPT, 2023 [5] |

## Writing and text input

Dzongkha uses the Tibetan script, with 30 consonants and 4 vowel signs [1]. Bhutan has 23 languages, 21 of them indigenous [1].

In August 2023, Dzongkha OCR and a spelling and grammar checker were "planned future upgrades" [6]. We found no Dzongkha-specific OCR model. Tibetan OCR models (BDRC, OpenPecha) may work on printed Dzongkha because the script is the same, but this is not tested.

## Data

- FineWeb-2 has 23,066 Dzongkha documents (32.15 MB) [10]. This is about seven times less than Tibetan in the same set.
- MADLAD-400 checked 1,899 Dzongkha documents. Its audit note says "maybe actually bo" (Tibetan) and "mainly buddhist vibes", and Dzongkha is not in its final table [11]. So some web text labelled Dzongkha may be Tibetan.
- The Bhutan government MT system was trained on about 700,000 parallel sentences from the Dzongkha Development Commission (DCDD) [7]. A GovTech talk mentions a "10 million sentence parallel corpus" for an earlier version [1]. These two numbers do not agree, and we could not check which is right.
- The licenses of these Bhutan datasets are not stated.

## Speech

- OpenAI Whisper does not list Dzongkha [8].
- Bhutan GovTech fine-tuned Meta MMS for Dzongkha. Speech to text (MMS-1B-All adapter, 7,385 training items) reached a word error rate (WER) of 0.373. Text to speech (mms-tts-dzo, 2,665 audio-text pairs) improved Mel Cepstral Distortion from 7 to 4.2 [1].
- Meta Omnilingual ASR (November 2025) reports a character error rate of 3.7 for Dzongkha, with 23.0 hours of training audio [9]. The test set is small, so this is a sign of support, not of real-world quality.

## Machine translation

**Support.** Google Translate added Dzongkha in June 2024 [2]. In the Google Cloud API it is NMT only, not in Google's Translation LLM [3]. Microsoft Translator does not support Dzongkha [4]. Meta NLLB-200 covers Dzongkha (dzo_Tibt) [12].

**Bhutan government system.** The College of Science and Technology (CST) launched the first Dzongkha MT system in August 2023, with "30 to 50 per cent" accuracy reported [6]. The current Dzongkha–English system is built on Meta NLLB and is "for testing and research only" [7]. A newer version based on NLLB-distilled-600M, Opus-MT and T5 is under test; the talk reports human evaluation but no scores [1].

**Benchmark: FLORES-200 devtest, English to Dzongkha, chrF++ (higher is better).**

| System | Score | Year | Source |
| --- | --- | --- | --- |
| NLLB-200 MoE | 34.7 | 2022 model, tested 2023 | [5] |
| NLLB-200 (likely 3.3B; copy of the official file, model not verified) | 32.6 | 2022 | [13] |
| ChatGPT (gpt-3.5) 5-shot | 15.9 | 2023 | [5] |
| ChatGPT (gpt-3.5) 0-shot | 7.7 | 2023 | [5] |

Google Translate was not scored for Dzongkha in that study [5]. These results are from 2023, and newer models may be much better. We found no public score for current frontier models. chrF++ scores can only be compared between systems in the same language and direction.

**Risk.** Because some web text labelled Dzongkha may be Tibetan [11], AI output may mix in Tibetan spelling and words. This is our inference, not a tested fact.

## AI projects

- Dzongkha NLP by Bhutan GovTech (Data Science and AI Division), with DCDD and CST: MT, speech to text, text to speech and a chatbot prototype [7] [1].
- A Dzongkha LLM pilot on Llama 3.1 8B, Qwen2.5 7B and DeepSeek 7B. The talk gives the training data as both "1.2 lakh" (120,000) and "only around 20k". An mT5 fine-tune reached 50% accuracy [1].

## Recommendation

To translate into Dzongkha today, use Google Translate as a baseline. Also test the Bhutan government NLLB system (research use only) and one current frontier model. A native Dzongkha reviewer must check all output, especially for Tibetan words and spellings. Confidence is low: the only scores are from 2023, and the government's own 2023 system reported 30 to 50 per cent accuracy.

Test first: FLORES+ devtest, English to Dzongkha, with chrF++, plus native review of 50 sentences per system. Then test a short Buddhist sample, such as prayers or a teaching summary. Dzongkha is not yet measured on the BuddhistAI leaderboard.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Dzongkha. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (2)

- [Dzongkha NLP (GovTech Bhutan)](https://v2.nlp.tech.gov.bt/background) (GovTech Agency Bhutan with DCDD and CST): Dzongkha-English machine translation built on Meta NLLB (about 700,000 sentence pairs), Dzongkha speech to text and text to speech, and a chatbot prototype. For testing and research only.
- [Dzongkha NLP (CST)](https://nlp.cst.edu.bt) (College of Science and Technology (Royal University of Bhutan) with DCDD): Web app with Dzongkha-English translation, Dzongkha speech to text and text to speech.

**Datasets** (0)

None listed yet.

<!-- in-directory:end -->

## Sources

1. [SANOG43: Dzongkha NLP (GovTech Bhutan and CST, slides)](https://www.sanog.org/resources/sanog43/SANOG43_Conference-Lightning-Dzongkha_NLP-Tenzin.pdf), read 2026-11-17
2. [Google Translate Help: more than 100 new languages](https://support.google.com/translate/answer/15139004?hl=en), read 2026-11-17
3. [Google Cloud Translation: Language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
4. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
5. [Robinson et al. 2023, arXiv 2309.07423](https://arxiv.org/pdf/2309.07423), read 2026-11-17
6. [ThePrint/ANI: Dzongkha machine translation system launched in Bhutan, 2023-08-10](https://theprint.in/world/dzongkha-machine-translation-system-launched-in-bhutan-to-digitise-national-language/1708463), read 2026-11-17
7. [Bhutan GovTech Dzongkha NLP: background](https://v2.nlp.tech.gov.bt/background), read 2026-11-17
8. [OpenAI Whisper tokenizer.py (language list)](https://raw.githubusercontent.com/openai/whisper/main/whisper/tokenizer.py), read 2026-11-17
9. [Meta Omnilingual ASR, per-language results (7B LLM-ASR)](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/per_language_results_table_7B_llm_asr.csv), read 2026-11-17
10. [FineWeb-2 README](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2/blob/cab26bb3cab1ca7c26bb13a48f80fc3d2def4620/README.md), read 2026-11-17
11. [MADLAD-400 README](https://huggingface.co/datasets/allenai/MADLAD-400/blob/f8e5ab9b4c80d211822840f9e1f3fe8079bea053/README.md?code=true), read 2026-11-17
12. [NLLB-200 1.3B model card](https://huggingface.co/facebook/nllb-200-1.3B/raw/main/README.md), read 2026-11-17
13. [Copy of the NLLB-200 metrics file (Mara4444/MSc_Thesis)](https://raw.githubusercontent.com/Mara4444/MSc_Thesis/main/datasets/others/nllb_metrics.csv), read 2026-11-17
