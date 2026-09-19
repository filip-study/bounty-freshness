# bounty-freshness

Tiny CLI: paste bounty issue URLs, get which ones are still **open**.

Built after we burned cycles on boards that list dollars on **closed** issues (Opire/Algora stale rows).

## Use

```bash
gh auth login   # once
printf '%s\n' \
  'https://github.com/tenstorrent/tt-metal/issues/56908' \
  'https://github.com/calcom/sans/issues/2' \
  > urls.txt
python3 bounty_freshness.py urls.txt
```


## Buy today's lane snapshot ($3 USDC)

Verified open vs stale paid lanes (this cycle):  
https://shieldz.cash/unlock/SUxX9gr_Yvxl8dQVbBQm

Tips: https://shieldz.cash/tip/tip-d2599a4d16a6f4b0

## Tip jar (optional)

Base USDC: `0xbAd41cF0f0d5442f9A53630F8081BFd257DA019b`


## Related (same wallet)

- [base-usdc-paylink](https://github.com/filip-study/base-usdc-paylink) — create Base USDC tip/unlock links

## License

MIT
