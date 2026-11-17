---
id: sanskrit
title: Sanskrit
kind: classical
group: Indic
countries: [India, Nepal]
scripts: [Devanagari, Roman]
speakers: about 20,000 users in India (Google 2022 [1])
directory_names: [Sanskrit]
resource_level: low
google_translate: yes (since 2022)
recommendation: Frontier LLM with retrieval and a Sanskrit reviewer
confidence: low
updated: 2026-11
contributors: []
---

# Sanskrit

Buddhist Sanskrit is the language of many Mahāyāna sūtras and śāstras, and of manuscripts kept in Nepal. There is good data for translation from Sanskrit into English, but every system was weak at writing Sanskrit in the tests we found.

## Summary

| | |
| --- | --- |
| Where | India and Nepal; scholars worldwide |
| Speakers | Google described Sanskrit as "used by about 20,000 people in India" (2022) [1] |
| Script | Devanagari; Roman (IAST) in scholarship |
| AI resources | low |
| Google Translate | yes, since 2022-05-11 [1]; NMT only in the Cloud API [2] |
| Microsoft Translator | no [3] |
| Speech to text | Whisper lists Sanskrit [4]; not in Meta Omnilingual ASR [5] |
| Best evidence on translation quality | FLORES-200, English to Sanskrit, 2023 [6] |

## Writing and text input

Sanskrit is written in Devanagari in India and Nepal. Scholars often use Roman letters with diacritics. Tools for sandhi splitting and lemmas (ByT5 Sanskrit analyzers, chronbmm data) and a Buddhist Sanskrit BERT model are listed in the Directory below. We did not verify OCR support for Sanskrit in this research.

## Data

- Buddhist Sanskrit texts: GRETIL and the Digital Sanskrit Buddhist Canon (DSBC) are listed in the Directory below.
- Mitrasaṃgraha (January 2026): 391,548 Sanskrit–English pairs, plus 5,587 validation and 5,552 test pairs. The full set is CC BY-NC-ND 4.0. A subset of 372,791 pairs is CC BY-SA 4.0 [7].
- MITRA-parallel: 1,742,786 sentence pairs between Sanskrit, Chinese and Tibetan, including 596,812 Sanskrit–Tibetan pairs [8].
- Sāmayik: about 53,000 English–Sanskrit pairs of modern prose. The license is not stated [9].
- Manuscripts: the Nepalese-German Manuscript Cataloguing Project (NGMCP) has a public catalogue with many Buddhist Sanskrit manuscripts. We saw it only in search results and did not open it.

Almost all parallel data and tests go from Sanskrit into English. Very little is made for English into Sanskrit.

## Speech

- OpenAI Whisper lists Sanskrit (sa) [4]. We did not find an error rate for it.
- Meta Omnilingual ASR has no Sanskrit language code [5].

## Machine translation

**Support.** Google Translate added Sanskrit on 2022-05-11 [1]. In the Google Cloud API it is NMT only [2]. Microsoft Translator does not support Sanskrit [3]. AI4Bharat's IndicTrans2 covers Sanskrit (san_Deva, about 278,000 training pairs) and aims at permissive licenses [10]. Meta NLLB-200 also covers Sanskrit [6].

**Benchmark: FLORES-200 devtest, English to Sanskrit, chrF++ (higher is better), 2023 [6].**

| System | Score |
| --- | --- |
| Google Translate | 30.3 |
| NLLB-200 MoE | 26.1 |
| ChatGPT (gpt-3.5) 5-shot | 22.6 |
| ChatGPT (gpt-3.5) 0-shot | 21.8 |

A copy of the NLLB-200 metrics file (model not verified, likely 3.3B) gives 25.6 [11]. All systems were weak. These are 2023 results, and newer models may be better. chrF++ can only be compared between systems in the same language and direction.

**Benchmark: Sāmayik, English to Sanskrit, chrF.** Best in-domain 46.61 (fine-tuned mBART); best out-of-domain 26.7 (fine-tuned IndicTrans) [9].

**Benchmark (opposite direction): Mitrasaṃgraha test set, Sanskrit to English, chrF / BLEURT / GEMBA (higher is better) [7].**

| System | chrF | BLEURT | GEMBA |
| --- | --- | --- | --- |
| Claude 3.7 Sonnet with retrieval (RAG) | 38.83 | 57.54 | 89.32 |
| Fine-tuned Gemma 2 9B | 38.36 | 55.10 | 83.34 |
| Gemini 2.0 Flash, zero-shot | 34.24 | 53.87 | 87.04 |
| Google Translate | 28.28 | 47.42 | 56.09 |

These scores show how well models read Sanskrit. They do not show how well models write Sanskrit.

## AI projects

- Dharmamitra: Mitrasaṃgraha and MITRA models (January 2026) [7] [8]. MITRA reports no scores for translation into Sanskrit [8].
- IndicTrans2 (AI4Bharat): open MT models for 22 Indian languages, including Sanskrit [10].
- Sanskrit analyzers and corpora are listed in the Directory below.

## Recommendation

To translate into Sanskrit today, use a current frontier model with retrieval (give it similar Sanskrit passages and a glossary). Use Google Translate and IndicTrans2 as baselines. A Sanskrit scholar must review all output. Confidence is low: the only into-Sanskrit scores are from 2023 and are low for every system.

Test first: FLORES+ devtest, English to Sanskrit, with chrF++, plus a Buddhist sample. For the sample, reverse 50 to 100 pairs from the Mitrasaṃgraha test set (English in, Sanskrit out) and ask a scholar to review 20 items. Check the license before you share any derived data. Sanskrit is not yet measured on the BuddhistAI leaderboard.

<!-- in-directory:start -->
## In the Directory

Projects and datasets in the [Directory](../directory/README.md) that list Sanskrit. This list is made from the Directory data. To add an entry, [suggest it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml).

**Projects** (16)

- [Dharmamitra](https://dharmamitra.org/) (Dharmamitra team (UC Berkeley and partners)): Machine translation, grammar analysis and search for Buddhist source languages. Its MITRA models are published on Hugging Face.
- [Dharmamitra dictionaries and lexicon](https://github.com/dharmamitra/dharmamitra-stardict-dictionaries) (Dharmamitra team): StarDict dictionaries and a lexicon built from Dharmamitra's parallel text collection.
- [Buddhist AI Translator (慧译通)](https://github.com/xr843/Buddhist-AI-Translator) (xr843 (community)): AI translator for Buddhist texts with support for Sanskrit, Pali and Tibetan terms.
- [BDRC - Buddhist Digital Resource Center](https://www.bdrc.io/) (BDRC): The largest digital library of Tibetan texts (scans, e-texts and catalog). In 2026 it started an initiative to build open Buddhist datasets for AI, and it publishes OCR models and datasets on Hugging Face.
- [SuttaCentral](https://suttacentral.net/) (SuttaCentral): Early Buddhist texts with parallels across languages and many translations. Texts and parallels are on GitHub (sc-data).
- [DharmaNexus](https://dharmanexus.org/) (Dharmamitra team (successor of BuddhaNexus)): Finds parallel and similar passages across the Pali, Sanskrit, Tibetan and Chinese canons.
- [FoJin](https://fojin.app/) (xr843 (community)): Buddhist text platform with more than 10,000 texts from over 600 sources and search across languages.
- [GRETIL](https://gretil.sub.uni-goettingen.de/) (Göttingen State and University Library): Collection of Sanskrit and other Indic e-texts, including many Buddhist texts.
- [Digital Sanskrit Buddhist Canon](https://www.dsbcproject.org/) (University of the West and partners): Sanskrit Buddhist texts in digital form.
- [Nepalese-German Manuscript Cataloguing Project (NGMCP)](https://ngmcp.fdm.uni-hamburg.de/mediawiki/index.php/NGMCP) (University of Hamburg with the National Archives of Nepal): Catalogue of the Nepalese manuscripts that the Nepal-German Manuscript Preservation Project microfilmed (more than 114,500 items in Sanskrit, Newari, Nepali and other languages).
- [ByT5 Sanskrit analyzers](https://github.com/dharmamitra/byt5-sanskrit-analyzers) (Dharmamitra team): Models for Sanskrit word splitting (sandhi), lemmas and grammar tags, and OCR post-correction.
- [MITRA models (buddhist-nlp)](https://huggingface.co/buddhist-nlp) (Dharmamitra team): About 60 models for Buddhist languages - translation (Gemma, Qwen, NLLB and mBART based), embeddings, sentence alignment, tagging and OCR.
- [Buddhist Sanskrit BERT](https://huggingface.co/Matej/bert-base-buddhist-sanskrit) (Matej (Hugging Face user)): BERT model trained on Buddhist Sanskrit texts.
- [Dharmamitra Claude Code agent](https://github.com/dharmamitra/dharmamitra-claude-code-agent) (Dharmamitra team): Starter pack for agent-based translation, critical editions and finding parallel passages.
- [Intellexus](https://www.kc-tbts.uni-hamburg.de/projects/intellexus.html) (University of Hamburg, Reichman University and partners): EU-funded research project on AI for Buddhist texts in Sanskrit and Tibetan. Makers of DharmaBench.
- [Tsadra Dharma AI Project](https://www.tsadra.org/ai-tools-for-tibetan-buddhist-translation/) (Tsadra Foundation with Dharmamitra): Webinars, slides and case studies on using AI tools in Tibetan translation work, and a Discord community for Dharma translation and AI.

**Datasets** (8)

- [DharmaBench](https://github.com/Intellexus-DSI/DharmaBench) (Intellexus (Reichman University, University of Hamburg)): 13 classification and span-detection tasks on Indian and Tibetan canonical texts, about 4,900 test items.
- [SuttaCentral data (sc-data)](https://github.com/suttacentral/sc-data) (SuttaCentral): Texts, translations and parallels behind SuttaCentral.
- [MITRA parallel data](https://github.com/dharmamitra/mitra-parallel) (Dharmamitra team): Parallel sentence data from the Dharmamitra project.
- [Mitrasaṃgraha](https://huggingface.co/datasets/buddhist-nlp/mitrasamgraha-released-data-only) (Dharmamitra team): Released part of the Dharmamitra parallel data collection. The paper version on GitHub (dharmamitra/mitrasamgraha-dataset) has 391,548 Sanskrit-English pairs with a test set.
- [Sāmayik](https://github.com/ayushbits/saamayik) (IIT Bombay, University of Utah and others): About 53,000 English-Sanskrit sentence pairs of modern prose, with training and evaluation scripts. Not Buddhist-specific.
- [Sanskrit sandhi, lemma and grammar data](https://huggingface.co/chronbmm) (chronbmm): Sanskrit datasets for splitting sandhi, lemmas, grammar tags and OCR post-correction.
- [Buddhist Philosophy Graph](https://huggingface.co/datasets/joyboseroy/buddhist-philosophy-graph) (joyboseroy (community)): Knowledge graph of nine Buddhist schools, from Theravada to Tibetan Vajrayana. Every link cites a named text with a quote.
- [MITRA instruction data](https://huggingface.co/datasets/buddhist-nlp/mitra-instructions) (Dharmamitra team): Instruction data from the MITRA project.

<!-- in-directory:end -->

## Sources

1. [Google blog: 24 new languages, 2022-05-11](https://blog.google/products/translate/24-new-languages/), read 2026-11-17
2. [Google Cloud Translation: Language support](https://docs.cloud.google.com/translate/docs/languages), read 2026-11-17
3. [Microsoft Learn: Translator language support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support), read 2026-11-17
4. [OpenAI Whisper tokenizer.py (language list)](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py), read 2026-11-17
5. [Meta Omnilingual ASR language IDs](https://raw.githubusercontent.com/facebookresearch/omnilingual-asr/main/src/omnilingual_asr/models/wav2vec2_llama/lang_ids.py), read 2026-11-17
6. [Robinson et al. 2023, arXiv 2309.07423](https://arxiv.org/pdf/2309.07423), read 2026-11-17
7. [Nehrdich et al., Mitrasaṃgraha, arXiv 2601.07314, 2026-01-12](https://arxiv.org/pdf/2601.07314), read 2026-11-17
8. [Nehrdich and Keutzer, MITRA, arXiv 2601.06400, 2026-01-10](https://arxiv.org/pdf/2601.06400), read 2026-11-17
9. [Sāmayik, arXiv 2305.14004 (Hugging Face papers page)](https://huggingface.co/papers/2305.14004.md), read 2026-11-17
10. [IndicTrans2, arXiv 2305.16307](https://arxiv.org/pdf/2305.16307), read 2026-11-17
11. [Copy of the NLLB-200 metrics file (Mara4444/MSc_Thesis)](https://raw.githubusercontent.com/Mara4444/MSc_Thesis/main/datasets/others/nllb_metrics.csv), read 2026-11-17
