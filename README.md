# WANIP

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]

A simple Home Assistant integration that exposes your public WAN IP address as a sensor entity. Updates every minute using the free [api.ipify.org](https://api.ipify.org) service — no account or API key required.

**✨ Develop in the cloud:** Want to contribute or customize this integration? Open it directly in GitHub Codespaces - no local setup required!

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/maxcharbonneau/ha-wanip?quickstart=1)

---

## ✨ Features

- **No credentials required**: Uses the free public API from api.ipify.org
- **Auto-updates**: Checks your WAN IP every minute
- **Change detection**: Only logs activity when your IP actually changes
- **Easy setup**: Single click, no YAML required

## 📦 What It Creates

Platform | Entity | Description
-- | -- | --
`sensor` | WAN IP Address | Your current public WAN IP address

---

## 🚀 Installation via HACS

**Prerequisites:** [HACS](https://hacs.xyz/) must be installed on your Home Assistant.

### Step 1: Add the repository

1. Open HACS in your Home Assistant
2. Click the **3 dots** menu → **Custom repositories**
3. Add `https://github.com/maxcharbonneau/ha-wanip` as an **Integration**
4. Search for **WANIP** and click **Download**
5. **Restart Home Assistant**

### Step 2: Add the integration

1. Go to **Settings** → **Devices & Services**
2. Click **"+ Add Integration"**
3. Search for **"WANIP"**
4. Click **Submit** — no credentials needed!

That's it! Your WAN IP sensor is ready. 🎉

---

## 📖 Manual Installation

1. Download the `custom_components/wanip/` folder from this repository
2. Copy it to your Home Assistant's `custom_components/` directory
3. Restart Home Assistant
4. Add the integration via **Settings** → **Devices & Services**

---

## 🔧 Troubleshooting

### Enable Debug Logging

Add the following to your `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.wanip: debug
```

### Common Issues

**Sensor shows unavailable**: Check your internet connection — the integration requires access to `api.ipify.org`.

---

## 🛠️ Development

Want to contribute? Open the project directly in GitHub Codespaces:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/maxcharbonneau/ha-wanip?quickstart=1)

- ✅ Zero local setup required
- ✅ Pre-configured development environment with Home Assistant
- ✅ 60 hours/month free for personal accounts

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with ❤️ by [@maxcharbonneau][user_profile]**

---

[commits-shield]: https://img.shields.io/github/commit-activity/y/maxcharbonneau/ha-wanip.svg?style=for-the-badge
[commits]: https://github.com/maxcharbonneau/ha-wanip/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/maxcharbonneau/ha-wanip.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40maxcharbonneau-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/maxcharbonneau/ha-wanip.svg?style=for-the-badge
[releases]: https://github.com/maxcharbonneau/ha-wanip/releases
[user_profile]: https://github.com/maxcharbonneau
