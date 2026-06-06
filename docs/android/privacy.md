# Privacy Policy

**Last Updated:** June 6, 2026

---

## 1. Introduction

This Privacy Policy explains how ColorCargo ("the App", "we", "us") collects, uses, and protects information when you use our mobile puzzle game on Android. We are committed to transparency, data minimization, and to keeping your privacy safe.

ColorCargo is **intended for a general-audience content rating** in the Google Play Store (Everyone / 3+) and is **not primarily directed to children under 13**. The App is designed for general audiences and does not require account creation. We do not operate any server backend; we hold **no personal data about you** on our infrastructure.

This Privacy Policy is reflected in the **Google Play Data safety** section on our Google Play store listing. We strive to keep both consistent.

For our Terms of Service, see [Terms of Service](colorcargo://terms).

---

## 2. Data We Collect

### 2.1 Data we collect directly

ColorCargo collects **minimal data** from you. The following is **Data Not Linked to Your Identity** (using the **Google Play Data safety** terminology) and is stored on your device. Where noted, limited in-app purchase data may also be carried over to a new device through **Android Auto Backup**, which is operated by Google and never transmitted to our servers:

- **Game progress**: Your current level, total moves, completed levels (stored locally on your device using **Android SharedPreferences**; **never transmitted to our servers**).
- **Sound preferences**: Whether you have toggled sounds on/off (stored locally).
- **Selected language**: Your in-game language preference (stored locally).

We **do not** collect: name, email, phone number, photos, contacts, location, health data, financial information, or any account credentials.

**In-app purchases** (where offered) are processed entirely by **Google Play Billing**. The App receives, **on device only**, limited purchase information such as the **transaction status** (success or failure), the **product identifier** of what you purchased, and the **purchase token / entitlement state** required to deliver the content; we **never receive your payment card details, billing address, or any Google account credentials**, and this information is **not transmitted to any server we operate**. See [Terms of Service](colorcargo://terms) Section 5 for the terms governing purchases.

Your **skip-ticket balance** (a consumable purchase) is stored on your device and may be **carried over to a new device through Android Auto Backup or device transfer** — for example, when you sign in with the same Google account during initial setup and Android restores a previous backup. **This is not real-time cross-device sync**; it is a reinstall / device-transfer / backup-restore mechanism, and the balance reflects whichever device most recently wrote a backup. **Remove Ads** is a non-consumable entitlement managed by **Google Play Billing**.

### 2.2 Data collected by third-party advertising networks

ColorCargo displays advertisements provided by **third-party ad networks** through the **Unity LevelPlay** mediation platform. **Google AdMob / Google Mobile Ads** may participate as an active bidding, ad-serving, and measurement partner through the LevelPlay AdMob Adapter where enabled in our mediation configuration. These networks may collect the following categories, which align with the **Google Play Data safety** categories:

- **Identifiers** — **Advertising ID (AAID)**, subject to your **Android ad personalization settings** and the regional privacy choices described in Section 2.4, and other device IDs as permitted by Android / Google Play
- **Device Information** — device model, **Android version**, screen size, system language, timezone, mobile carrier (where exposed)
- **Approximate Location** — ad partners may derive your approximate location from your IP address for geographic ad targeting and fraud prevention. ColorCargo itself requests no location permission and does not access device GPS. Advertising partners participating in the IAB TCF may request precise geolocation consent in the consent form; you can decline it. Because the App does not request location permission, it does not provide GPS-level location data to advertising partners through the App.
- **Usage Data** — ad interaction events (impressions, clicks, view completions, skip events, dwell time)
- **Diagnostics** — crash and performance data internal to each ad SDK

The ad mediation platform and active ad-serving or bidding partners currently integrated or enabled are listed below. **Unity LevelPlay** serves advertisements from Unity's own demand sources (including the **ironSource Exchange**) and may include additional partner networks where enabled. **Google AdMob / Google Mobile Ads** may serve, bid on, or measure ads through the LevelPlay AdMob Adapter and **Google Mobile Ads SDK** where enabled. **Additional ad networks may be enabled in future updates**; if so, this Privacy Policy will be revised and the change highlighted in the App's release notes. Active partners at any given time are determined by our **mediation configuration and bundled SDKs**.

| Ad mediation / ad-serving partner | Privacy Policy |
|---|---|
| Unity LevelPlay (Unity Technologies) | [unity.com/legal/game-player-and-app-user-privacy-policy](https://unity.com/legal/game-player-and-app-user-privacy-policy) |
| Google AdMob / Google Mobile Ads (Google LLC) | [policies.google.com/technologies/ads](https://policies.google.com/technologies/ads) and [policies.google.com/privacy](https://policies.google.com/privacy) |

### 2.3 Android Advertising ID and ad personalization

On Android, ColorCargo does **not** display a separate per-app tracking prompt — Android does not have an equivalent system prompt. Instead, ad personalization is controlled by your **Android Advertising ID (AAID)** settings and, where applicable, the Google UMP regional privacy choices described in Section 2.4.

- **By default**, ad partners may use your Advertising ID (AAID) to deliver personalized advertising, subject to your Google account's ad personalization settings and any regional consent choices.
- You can **reset or delete your Advertising ID at any time** via **Android Settings → Privacy → Ads → Reset advertising ID / Delete advertising ID** (the exact path may vary by device manufacturer and Android version).
- You can also manage Google ad personalization at [adssettings.google.com](https://adssettings.google.com/).
- ColorCargo does **not** use device fingerprinting or any other indirect method to track you across other companies' apps and websites. If the Advertising ID is unavailable or you have opted out of personalization, ads still appear, but they are **contextual or non-personalized** rather than tailored to you.

### 2.4 Regional advertising consent and privacy choices

If you access the App from a region where an advertising consent or privacy-choice message is required or configured, the App uses **Google User Messaging Platform (UMP)** to request and manage the applicable choices. This may include consent choices for the **European Economic Area (EEA), the United Kingdom, and Switzerland** under the GDPR, UK GDPR, Swiss FADP, and the ePrivacy Directive, and privacy choices for **supported US states** where applicable.

- **If you consent:** our ad partners may use your data — including, subject to your Android ad personalization settings, your Advertising ID (AAID) — to deliver personalized advertising.
- **If you do not consent:** advertising may be **non-personalized, limited, or unavailable**, depending on partner availability. The App remains fully playable in all cases.

Some partners may rely on consent or legitimate interests where permitted; you can review and manage these choices in the privacy options form.

These regional consent choices operate alongside, and may interact with, your **Android Advertising ID and ad personalization settings** (Section 2.3); depending on your choices and your region, both may apply.

You can **review or change your advertising consent or privacy choices at any time** from **Settings → Privacy Choices** inside the App, which reopens the Google UMP privacy options form when available. This option is shown when UMP reports that a privacy options entry point is required, including for EEA, UK, Switzerland, and supported US state privacy choices where applicable.

---

## 3. How We Use Data

We use the data above strictly to:

- Display advertisements (personalized only where permitted by your regional consent or privacy choices and your Android ad personalization settings; otherwise contextual)
- Measure ad effectiveness and prevent fraud (handled by ad networks; we do not access raw device-level data)
- **Verify in-app purchase transactions on device** via **Google Play Billing** (where in-app purchases are offered) — solely to deliver purchased content to your device and to support the **Restore Purchases** function on reinstall or on a new device
- Improve App stability and performance via the diagnostics built into the integrated ad SDKs (Section 2.2). ColorCargo itself does not embed an additional crash reporter; you can manage Android system usage & diagnostics data sharing in **Android Settings → Privacy → Usage & diagnostics**

We do **not** profile users for purposes beyond basic ad targeting. We do **not** use your data for marketing communications, data brokering, or training AI models.

---

## 4. Data Sharing

Data is shared only with:

- **Ad partners and mediation/ad-serving platforms** (Section 2.2) — strictly limited to the data needed for ad serving, bidding, attribution, measurement, and fraud prevention. We require our ad partners, including **Unity LevelPlay**, **Google AdMob / Google Mobile Ads**, and active ad technology partners, through applicable SDK and platform terms, **to handle your data consistent with this Privacy Policy, the Google Play Developer Program Policies (in particular the User Data and Families policies), and applicable privacy laws (GDPR, UK GDPR, Swiss FADP, CCPA/CPRA, COPPA, KVKK, and similar regional frameworks)**.
- **Google** — for **Google Play Billing** (purchase processing) and limited Google Play services diagnostics that you control in Android system Settings.

We do **not** share data with: data brokers, social-media platforms (unless you initiate sharing yourself, for example by screenshotting), generative-AI service providers, or any other third party.

### 4.1 California "Sale" and "Sharing" of Personal Information

We do **not sell your personal information for monetary compensation**. Under the California Consumer Privacy Act (CCPA) and California Privacy Rights Act (CPRA), our disclosure of limited device and ad-interaction data to ad partners for cross-context behavioral advertising may qualify as "sharing." You can opt out of this "sharing" at any time by:

1. Using **Settings → Privacy Choices** inside the App where this option is shown for your region,
2. Resetting or deleting your **Advertising ID** in **Android Settings → Privacy → Ads** and adjusting your Google ad personalization at [adssettings.google.com](https://adssettings.google.com/), or
3. Contacting us at **onuragames@gmail.com** with the subject line "Do Not Share – California Resident".

---

## 5. Data Retention

- **Local data** (game progress, settings) remains on your device until you delete the App. **Deleting the App wipes all local data permanently.** Note that, if **Android Auto Backup** is enabled for the App on your device, certain local preferences (such as your skip-ticket balance) may be restored automatically when you reinstall the App and sign in with the same Google account, or when you set up a new device.
- **Ad-related data** is retained by our ad partners (Section 2.2) **according to each partner's own published retention schedule**. We do not control or have visibility into these schedules; please refer to each partner's privacy policy for specifics.
- **No data is stored on our servers** because we do not operate any servers for user data.

---

## 6. Your Rights

In addition to the universal rights below, residents of certain regions have additional statutory rights (see Section 6.1).

Universal rights — available to **all users**:

- **Reset or delete your Advertising ID** at any time via **Android Settings → Privacy → Ads**, and manage Google ad personalization at [adssettings.google.com](https://adssettings.google.com/)
- **Review or change advertising consent/privacy choices** via Settings → Privacy Choices where shown, including EEA, UK, Switzerland, and supported US state privacy choices where applicable
- **Delete all local data** by uninstalling the App
- **Report inappropriate ads** via Settings → [Report Ad](colorcargo://report-ad) inside the App (consistent with the Google Play Families Policy and ad-network requirements)
- **Contact us** with privacy questions at **onuragames@gmail.com** — we will respond within a reasonable timeframe (and within statutory deadlines where applicable; see Section 6.1)
- **Request information from ad partners** directly. Because ColorCargo holds **no personal data about you on its own servers**, requests for access, deletion, correction, or portability of *ad-related* data must be exercised against each network using the privacy-policy links in Section 2.2.

### 6.1 Regional Privacy Rights

**European Economic Area, United Kingdom, and Switzerland (GDPR / UK GDPR / FADP):**

If you reside in the EEA, the UK, or Switzerland, you have the right to:

- **Access** the personal data held about you
- **Rectify** inaccurate or incomplete data
- **Erasure** ("right to be forgotten")
- **Restrict** or **object** to certain types of processing
- **Data portability** (where applicable and technically feasible)
- **Withdraw consent** at any time, without affecting the lawfulness of processing carried out before withdrawal
- **Lodge a complaint** with your local data protection authority (for the UK: the [ICO](https://ico.org.uk/); for Ireland: the [DPC](https://www.dataprotection.ie/); for other Member States: see the [EDPB list](https://edpb.europa.eu/about-edpb/about-edpb/members_en))

Because ColorCargo holds no personal data on its own backend, most of these rights are exercised **against the ad networks listed in Section 2.2**, who act as data controllers (or joint controllers) for the data they collect. Contact us at **onuragames@gmail.com** for assistance navigating these requests.

We will respond to verifiable requests within **30 days** (extendable by 60 additional days where permitted by GDPR Article 12).

**California (CCPA / CPRA):**

California residents have the right to:

- **Know** what personal information is collected, how it is used, and to whom it is disclosed
- **Delete** personal information (limited by the fact that we hold none directly; see Section 6 universal rights)
- **Correct** inaccurate personal information
- **Opt out of "sale" or "sharing"** of personal information for cross-context behavioral advertising (see Section 4.1)
- **Limit the use and disclosure of sensitive personal information**
- **Non-discrimination** for exercising any of these rights

We will respond to verifiable California requests within **45 days** (extendable by 45 additional days where permitted by CCPA § 1798.130).

**Türkiye (KVKK — Personal Data Protection Authority):**

If you reside in Türkiye, KVKK Article 11 grants you the rights to:

- Learn whether your personal data is being processed
- **If your personal data has been processed, request information about such processing**
- Request information about the purposes of processing and whether it has been used in accordance with such purposes
- Learn the third parties to whom data is transferred (domestically or abroad)
- Request correction, erasure, or destruction of processed data
- **Request that any correction, erasure, or destruction be communicated to third parties to whom your data has been transferred**
- Object to results arising solely from automated systems
- Demand compensation for damages caused by unlawful processing
- Lodge a complaint with the **Personal Data Protection Authority** via [kvkk.gov.tr](https://www.kvkk.gov.tr/)

Contact us at **onuragames@gmail.com** to exercise these rights.

**Other regions:** If you reside in a jurisdiction with additional privacy rights (e.g., Brazil LGPD, Canada PIPEDA, Australia Privacy Act, India DPDP, China PIPL), comparable rights may apply. Contact us and we will respond in accordance with applicable law.

---

## 7. Children's Privacy

ColorCargo is **intended for a general-audience content rating** in the Google Play Store (Everyone / 3+) but is **not primarily directed to children under 13**. We do **not knowingly collect** personal information from children under 13 within the meaning of the Children's Online Privacy Protection Act (COPPA) or analogous laws in other jurisdictions.

If we learn that personal information of a child under 13 has been inadvertently collected through one of our ad partners, we will work with the relevant network to delete or disable such information and, where required, to apply non-behavioral (contextual) advertising for that user.

Ads delivered via our mediation platform are required by the **Google Play Developer Program Policies and our agreements with each ad network** to be appropriate for the App's general-audience rating. Inappropriate ads may still slip through occasionally; please use **Settings → [Report Ad](colorcargo://report-ad)** to flag them, or email **onuragames@gmail.com**.

Parents and guardians can disable behavioral advertising for their household via **Android device parental controls, the Family Link app, and the device's content & privacy restrictions**, and by **resetting or deleting the Advertising ID** in Android Settings → Privacy → Ads.

---

## 8. Security

We do not transmit user data to our own servers, so the primary security surface is limited to:

- Your device's local storage, protected by **Android app sandboxing** and (where you have enabled it) the device lock / biometric authentication (fingerprint, face, etc.)
- The third-party ad network connections, which use **HTTPS-encrypted transports** as required by the Android network security configuration and Google Play policy

We do not have access to any breach reporting mechanism, because we hold no personal data ourselves. If a breach occurs at one of our ad partners, that partner is responsible for notifying you in accordance with applicable law (e.g., GDPR Article 33, CCPA § 1798.82).

---

## 9. Changes to This Policy

We may update this Privacy Policy as needed (e.g., when adding new ad networks, features, or legal sections). The **"Last Updated"** date at the top of this document will reflect the most recent revision. Significant changes will be highlighted in the App's Google Play release notes and on our Google Play store listing.

Your continued use of the App after such updates constitutes acceptance of the revised Policy.

---

## 10. Contact

Questions, concerns, or rights requests? Contact us at:

**onuragames@gmail.com**

We aim to respond within a reasonable timeframe, and within the statutory deadlines set out in Section 6.1 where they apply.

---

## 11. Governing Law

This Privacy Policy is governed by the laws of the **Republic of Türkiye**, without regard to conflict of laws principles. Nothing in this Policy limits any mandatory consumer-protection or data-protection rights granted to you under the law of your country of residence.

---

## 12. App Information

- **App:** ColorCargo
- **Developer:** Onur Akçakavak
- **Contact:** onuragames@gmail.com
- **Effective Date:** June 6, 2026
