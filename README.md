# Flight Deals Finder

A Python application that checks your ideal flight prices for destinations stored in a Sheety-connected Google Sheet. When a destination's current price is below your target price, the application sends a WhatsApp notification using Twilio.

## How it works

1. Reads destination IATA codes and target prices from your Sheety endpoint.
2. Searches Google Flights through SerpAPI for each destination.
3. Compares the lowest available price with your target price.
4. Sends a WhatsApp alert through Twilio when a cheaper fare is found.

## Requirements

- Python 3.9 or newer
- A [SerpAPI](https://serpapi.com/) account and API key
- A [Sheety](https://sheety.co/) project connected to a Google Sheet
- A [Twilio](https://www.twilio.com/) account with the WhatsApp Sandbox configured
- A phone/WhatsApp account joined to your Twilio Sandbox

## Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Configure environment variables

Create your local environment file from the example.

### macOS / Linux

```bash
cp .env.example .env
```

### Windows (PowerShell)

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace every placeholder with your own credentials and settings.

| Variable               | Description                                                       |
|------------------------|-------------------------------------------------------------------|
| `SERPAPI_APIKEY`       | API key from your SerpAPI account                                 |
| `SHEETY_TOKEN`         | Bearer token generated for your Sheety project                    |
| `TWILIO_ACC_SID`       | Twilio Account SID                                                |
| `TWILIO_AUTH_TOKEN`    | Twilio Auth Token                                                 |
| `TWILIO_FROM_WHATSAPP` | Twilio WhatsApp sender for the Sandbox                            |
| `TWILIO_TO_WHATSAPP`   | Your WhatsApp number in international format                      |
| `DEPARTURE_IATA`       | Three-letter IATA code for the departure airport (example: `BLR`) |
| `OUTBOUND_DATE`        | Flight departure date in `YYYY-MM-DD` format                      |

**Important:** Do not add quotation marks around ordinary `.env` values unless the value itself needs quoting.

## Prepare your Google Sheet / Sheety data

The Sheety endpoint should return a JSON object containing a `flight` array. Each row should have these fields:

| city | iataCode | lowestPrice |
|---|---|---:|
| Paris | PAR | 55000 |
| Tokyo | TYO | 45000 |

The `lowestPrice` column is your target price in **INR**.

Make sure the endpoint in `SHEETY_ENDPOINT` points to the correct Sheety project, sheet, and worksheet resource. The code expects the response key to be `flight`.

## Configure Twilio WhatsApp

1. Set up the WhatsApp Sandbox in your Twilio Console.
2. Follow Twilio's instructions to join the Sandbox from the WhatsApp number that should receive alerts.
3. Put the Sandbox sender and your joined recipient number in `.env`.
4. Confirm your Twilio account has the required permissions and balance/configuration to send messages.
5. Update `TWILIO_WHATSAPP_FROM` with the number provided by the sandbox accordingly.

## Run the application

Make sure your virtual environment is activated and `.env` is in the same directory as `main.py`, then run:

```bash
python main.py
```

The application prints the lowest price found for each destination. It sends a WhatsApp alert only when the returned price is lower than the target price in the sheet.

## Project structure

```text
flight-deals/
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Troubleshooting

- **Missing environment variable:** Check that `.env` exists in the project root and that the variable names match `.env.example`.
- **401 / 403 response:** Check the relevant API key, token, permissions, and account status.
- **Sheety response has no `flight` key:** Verify the endpoint and the worksheet/resource name.
- **No price insight returned:** Check the SerpAPI response, destination IATA code, date, and search parameters. Google Flights results can vary.
- **WhatsApp message not sent:** Check that both WhatsApp numbers include the `whatsapp:` prefix and that the recipient has joined the Sandbox.
