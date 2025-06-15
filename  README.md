# Amazon Price Watcher Home Assistant Integration

This custom integration connects your local Amazon Price Watcher Flask API to Home Assistant.

## Features

- Creates a sensor for each tracked Amazon product (shows price, title, availability, last checked)
- Add/remove products via service calls
- HACS-ready

## Installation

1. Copy this folder to `custom_components/amazon_price_watcher` in your Home Assistant config.
2. Restart Home Assistant.
3. Add the integration via YAML or UI (if config flow is added).
4. Configure your Flask API host in `const.py` if not running on `localhost:5000`.

## Example sensor config (YAML)

```yaml
sensor:
  - platform: amazon_price_watcher
```

## Services

- `amazon_price_watcher.add_product` (fields: url)
- `amazon_price_watcher.remove_product` (fields: product_id)

## HACS

Add this repo as a custom repository in HACS for easy updates.

## License

MIT