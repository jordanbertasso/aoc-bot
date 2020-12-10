# AoC Solve Bot Discord
This is a dockerised bot that uses Discords channel webhook feature to announce AoC solves.

## Usage
1. [Create a Discord channel webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) for the channel where you want the solves to be announced and copy the webhook link.

2. Update `config.py` with the webhook link, AoC session token and the API endpoint for your AoC.

3. Start with
    ```
    make run
    ```

You can customise the announcement template in `config.py` as well.
