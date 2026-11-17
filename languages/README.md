---
title: Languages
summary: "AI resources and AI quality for each Buddhist language, and an overview of Buddhist countries and regions."
wide: true
permalink: /languages/
---

# Languages: AI resources for Buddhist languages

This section shows, for each Buddhist language, what data exists, who is building AI for it, and how well today's AI can translate into it. Use it to choose an AI system before you translate Buddhist material into a language, and to find gaps that need data or a benchmark.

There is one page per language, and a table of Buddhist countries and regions below. Each language page lists its projects and datasets from the [Directory](../directory/README.md) automatically.

> **Short answer (November 2026).** For Chinese, Japanese, Korean, Vietnamese and Thai, all major AI systems translate well, and the main risk is Buddhist terms. For Burmese, Lao, Khmer, Sinhala, Nepali and Mongolian, the large AI models from Google, OpenAI and Anthropic are usable but need a native reviewer. For Tibetan, Dzongkha, Sanskrit and Newari, quality is low and there is no good public test of translation into these languages. For Pali, Buryat, Kalmyk, Tuvan, Ladakhi and the other Himalayan languages, there is almost no data and no test, so a human translator must lead. In every case, test a few systems on your own sample before you choose.

**How to read the tables.**

- **AI resources** is our judgement of how much data and AI support a language has: high, medium, low or very low. It is based on vendor support and published tests, not on our own measurement.
- **Google Translate** says if Google supports the language and since when.
- **To translate into it, use** is the current best option from the published evidence. **Confidence** says how strong that evidence is. "Low" means there is no real test, only support lists or a few reports.
- **Directory** is the number of projects and datasets in the Directory for that language.

**Read the evidence with care.**

- Most published translation scores are from 2023 to 2025. Newer models may be better.
- Scores such as chrF++ and BLEU can only be compared between systems in the same language and direction. A lower score in Japanese than in Lao does not mean Japanese is worse: the scores depend on the script and the test.
- Almost no test uses Buddhist text. General scores show if a model can write the language, not if it uses Buddhist terms correctly.
- We have not yet measured these languages on the [BuddhistAI leaderboard](https://buddhistai.github.io/buddhist-benchmarks/). If you can help build a small translation test for a language, [open an issue](https://github.com/BuddhistAI/knowledge-base/issues/new) or see the [translation task](../tasks/translation.md).

**How this was made.** The pages were written on 17 November 2026 from web research on published papers, vendor language lists, Hugging Face and project sites. Every fact has a source on its page. Where we could not check a fact, the page says "not verified". Please correct anything that is wrong with "Edit this page".

<!-- languages:start -->
## Languages

| Language | Kind | Where | Speakers | AI resources | Google Translate | To translate into it, use | Confidence | Directory |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Dzongkha](dzongkha.md) | modern | Bhutan | not verified | low | yes (since 2024) | Google Translate as a baseline with native review | low | 2 |
| [Ladakhi and other Himalayan languages](himalayan-tibetic.md) | modern | India, Nepal, Pakistan | not verified | very low | no | Human translation; AI only for drafts | low | 0 |
| [Tibetan](tibetan.md) | classical and modern | China, India, Nepal, Bhutan | not verified | low | yes (since 2024) | Google or Microsoft as a baseline with a human translator | low | 70 |
| [Nepali](nepali.md) | modern | Nepal, India, Bhutan | about 32 million (19 million first language; Wikipedia) | medium | yes (year not verified) | Google Translate or a frontier LLM; IndicTrans2 as open option | medium | 1 |
| [Newari (Nepal Bhasa)](newari.md) | classical and modern | Nepal | about 880,000 native speakers (2021 census; Wikipedia) | low | yes (since 2024) | Google Translate plus a frontier LLM with native review | low | 2 |
| [Pali](pali.md) | classical | Sri Lanka, Myanmar, Thailand, Cambodia, Laos | not applicable (liturgical language) | very low | no | Frontier LLM with a glossary and a Pali reviewer | low | 33 |
| [Sanskrit](sanskrit.md) | classical | India, Nepal | about 20,000 users in India (Google 2022) | low | yes (since 2022) | Frontier LLM with retrieval and a Sanskrit reviewer | low | 24 |
| [Sinhala](sinhala.md) | modern | Sri Lanka | about 20 million (18 million first language; Wikipedia) | medium | yes (year not verified) | Google Translate or a frontier LLM with a Sinhala reviewer | medium | 6 |
| [Burmese](burmese.md) | modern | Myanmar | about 33 million first language and 10 million second language (2019; Wikipedia) | medium | yes | Gemini 2.5 Pro or newer with Unicode checks and native review | medium | 4 |
| [Khmer](khmer.md) | modern | Cambodia | about 21 million incl. second-language speakers (2019 and 2024; Wikipedia, no source named) | medium | yes | Frontier LLM or Google Translate after a side-by-side test | low | 5 |
| [Lao](lao.md) | modern | Laos, Thailand | about 3.7 million first language and 0.8 million second language (2015; Wikipedia, no source named) | medium | yes | Gemini (2.5 Pro or 3 Pro) with a glossary and native review | medium | 3 |
| [Thai](thai.md) | modern | Thailand | about 71 million incl. second-language speakers (2024; Wikipedia) | high | yes | Frontier LLM with a Buddhist glossary and monastic review | medium | 13 |
| [Chinese](chinese.md) | modern | China, Taiwan, Hong Kong, Singapore, Malaysia | Mandarin about 1.18 billion and Cantonese about 86 million (Ethnologue 2026) | high | yes (Simplified and Traditional; Cantonese NMT only) | Frontier LLM with a Buddhist glossary and native review | medium | 12 |
| [Classical Chinese](classical-chinese.md) | classical | China, Taiwan, Hong Kong, Japan, South Korea, Vietnam | not verified (a written language with no native speakers) | medium | not verified | Frontier LLM with RAG over CBETA and DDB; compare with MITRA | low | 32 |
| [Japanese](japanese.md) | modern | Japan | about 126 million (Ethnologue 2026) | high | yes (Translation LLM and NMT) | Frontier LLM with a Buddhist glossary and native review | medium | 4 |
| [Korean](korean.md) | modern | South Korea, North Korea | about 82 million (Ethnologue 2026) | high | yes (Translation LLM and NMT) | Frontier LLM with a Buddhist glossary and native review | medium | 0 |
| [Vietnamese](vietnamese.md) | modern | Vietnam | about 97 million (Ethnologue 2026) | high | yes (Translation LLM and NMT) | Frontier LLM with a Hán-Việt glossary and native review | low | 3 |
| [Buryat](buryat.md) | modern | Russia, Mongolia, China | 130,500 to 440,000; sources disagree (2010 census and Wikipedia infobox) | very low | yes (since 2024) | Google Translate or Yandex compared with a frontier LLM on a small test | low | 2 |
| [Kalmyk](kalmyk.md) | modern | Russia | about 110,000 (2021 Russian census; Wikipedia) | very low | no | Frontier LLM with full native post-editing | low | 1 |
| [Mongolian](mongolian.md) | classical and modern | Mongolia, China, Russia | about 5 million native speakers (2020 to 2022; Wikipedia) | medium | yes (Cyrillic only) | Frontier LLM (Gemini first) in Cyrillic with native review | medium | 1 |
| [Tuvan](tuvan.md) | modern | Russia, China | about 253,000 native speakers (2020; Rosstat via Wikipedia) | very low | yes (since 2024) | Google Translate or Yandex compared with a frontier LLM on a small test | low | 2 |

## Countries and regions

| Country or region | Buddhists | Main traditions | Languages | Source |
| --- | --- | --- | --- | --- |
| **South Asia and the Himalayas** | | | | |
| Bhutan | about 75% (2020) | Vajrayana (Drukpa Kagyu, Nyingma) | [Tibetan](tibetan.md), [Dzongkha](dzongkha.md), [Ladakhi and other Himalayan languages](himalayan-tibetic.md) | [source](https://www.pewresearch.org/religion/2025/06/09/buddhist-population-change/) |
| Tibet (Tibet Autonomous Region and Tibetan areas of China) | not verified | Vajrayana (Gelug, Kagyu, Nyingma, Sakya) | [Tibetan](tibetan.md), [Sanskrit](sanskrit.md), [Chinese](chinese.md) | [source](https://en.wikipedia.org/wiki/Buddhism_by_country) |
| Tibetan diaspora (India and Nepal) | about 94,200 Tibetans in India and 13,500 in Nepal (2009 survey of Tibetans in exile; counts people, not religion) | Vajrayana (Gelug, Kagyu, Nyingma, Sakya) | [Tibetan](tibetan.md), [Sanskrit](sanskrit.md) | [source](https://en.wikipedia.org/wiki/Tibetan_diaspora) |
| Ladakh and Himalayan India | about 66% in Leh district, Ladakh (2011 census) | Vajrayana (Drikung Kagyu, Drukpa Kagyu, Gelug; Nyingma and Karma Kagyu in Sikkim) | [Tibetan](tibetan.md), [Ladakhi and other Himalayan languages](himalayan-tibetic.md), [Nepali](nepali.md) | [source](https://www.census2011.co.in/data/religion/district/621-leh.html) |
| Nepal | 8.2%, about 2.39 million (2021 census) | Vajrayana (Tibetan schools and Newar Buddhism); Theravada revival | [Sanskrit](sanskrit.md), [Tibetan](tibetan.md), [Pali](pali.md), [Nepali](nepali.md), [Newari (Nepal Bhasa)](newari.md), [Ladakhi and other Himalayan languages](himalayan-tibetic.md) | [source](https://theprint.in/world/nepals-81-19-per-cent-population-is-hindu-even-as-followers-of-hinduism-buddhism-decline-and-islam-christians-increase/1611622) |
| Sri Lanka | about 70% (2020) | Theravada | [Pali](pali.md), [Sinhala](sinhala.md) | [source](https://www.pewresearch.org/religion/2025/06/09/buddhist-population-change/) |
| **Mainland Southeast Asia** | | | | |
| Myanmar | about 89% (2020) | Theravada | [Pali](pali.md), [Burmese](burmese.md) | [source](https://www.pewresearch.org/religion/2025/06/09/buddhist-population-change/) |
| Thailand | about 94%, 68 million (2020) | Theravada (Maha Nikaya, Dhammayuttika Nikaya) | [Pali](pali.md), [Thai](thai.md) | [source](https://www.pewresearch.org/religion/2025/06/09/buddhist-population-change/) |
| Laos | about 64% (2020) | Theravada | [Pali](pali.md), [Lao](lao.md) | [source](https://www.pewresearch.org/religion/2025/06/09/buddhist-population-change/) |
| Cambodia | about 97% (2020) | Theravada | [Pali](pali.md), [Khmer](khmer.md) | [source](https://www.pewresearch.org/religion/2025/06/09/buddhist-population-change/) |
| Vietnam | about 23% (2020, Pew estimate as reported by Wikipedia) | Mahayana (Thien/Zen, Pure Land); Theravada among Khmer Krom | [Classical Chinese](classical-chinese.md), [Pali](pali.md), [Vietnamese](vietnamese.md), [Khmer](khmer.md) | [source](https://en.wikipedia.org/wiki/Buddhism_by_country) |
| **East Asia** | | | | |
| China (mainland) | about 4%, 53 million (2020) | Mahayana (Chan, Pure Land, Tiantai, Huayan) | [Classical Chinese](classical-chinese.md), [Chinese](chinese.md) | [source](https://www.pewresearch.org/religion/2025/06/09/buddhist-population-change/) |
| Taiwan | about a quarter of adults (2023 survey) | Mahayana (Pure Land, Chan, humanistic Buddhism) | [Classical Chinese](classical-chinese.md), [Chinese](chinese.md) | [source](https://www.pewresearch.org/short-reads/2024/07/29/4-facts-about-religion-and-diversity-in-taiwan/) |
| Hong Kong | more than 1 million followers (2016 government fact sheet) | Mahayana (Chan, Pure Land) | [Classical Chinese](classical-chinese.md), [Chinese](chinese.md) | [source](https://www.cstb.gov.hk/file_manager/en/documents/consultation-and-publications/hong_kong_fact_sheets.pdf) |
| Japan | about 37% (2020, Pew estimate as reported by Wikipedia) | Mahayana (Pure Land, Zen, Nichiren, Shingon, Tendai) | [Classical Chinese](classical-chinese.md), [Japanese](japanese.md) | [source](https://en.wikipedia.org/wiki/Buddhism_by_country) |
| South Korea | about 19% (2020) | Mahayana (Seon/Zen, mainly the Jogye Order) | [Classical Chinese](classical-chinese.md), [Korean](korean.md) | [source](https://www.pewresearch.org/religion/2025/06/09/buddhist-population-change/) |
| **Inner Asia and Russia** | | | | |
| Mongolia | about 51% (2020) | Vajrayana (mainly Gelug) | [Tibetan](tibetan.md), [Mongolian](mongolian.md) | [source](https://www.pewresearch.org/religion/2025/06/09/buddhist-population-change/) |
| Inner Mongolia (China) | not verified | Vajrayana (mainly Gelug) | [Tibetan](tibetan.md), [Mongolian](mongolian.md), [Chinese](chinese.md) | [source](https://en.wikipedia.org/wiki/Buddhism_by_country) |
| Buryatia (Russia) | about 20% (2012 survey) | Vajrayana (mainly Gelug) | [Tibetan](tibetan.md), [Buryat](buryat.md), [Mongolian](mongolian.md) | [source](https://en.wikipedia.org/wiki/Buryatia) |
| Kalmykia (Russia) | about 48% (2012 survey) | Vajrayana (mainly Gelug) | [Tibetan](tibetan.md), [Kalmyk](kalmyk.md) | [source](https://en.wikipedia.org/wiki/Kalmykia) |
| Tuva (Russia) | about 62% (2012 survey) | Vajrayana (mainly Gelug) | [Tibetan](tibetan.md), [Tuvan](tuvan.md) | [source](https://en.wikipedia.org/wiki/Tuva) |
| **Other countries with large Buddhist communities** | | | | |
| Singapore | 31.1% of residents aged 15 and over (2020 census) | Mahayana (Chinese schools); also Theravada and Vajrayana | [Classical Chinese](classical-chinese.md), [Pali](pali.md), [Chinese](chinese.md) | [source](https://www.singstat.gov.sg/-/media/files/publications/cop2020/sr1/executive-summary.pdf) |
| Malaysia | 18.7% (2020 census) | Mahayana (Chinese schools); also Theravada and Vajrayana | [Classical Chinese](classical-chinese.md), [Pali](pali.md), [Chinese](chinese.md) | [source](https://www.sinardaily.my/ampArticle/171461) |
| India (overall) | about 10 million, less than 1% (2020) | Navayana (Ambedkarite Buddhism, mainly in Maharashtra); Vajrayana in the Himalayas; Theravada | [Pali](pali.md), [Sanskrit](sanskrit.md), [Tibetan](tibetan.md) | [source](https://www.pewresearch.org/religion/2025/06/09/buddhist-population-change/) |
<!-- languages:end -->
