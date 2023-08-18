# fitness-tracking

## Quickstart

```bash
git clone git@gitlab.com:christian.kesler/fitness-tracking.git
cd fitness-tracking
git remote set-url --add --push origin git@github.com:christian-kesler/fitness-tracking.git
git remote set-url --add --push origin git@gitlab.com:christian.kesler/fitness-tracking.git
```


```bash
python3 graphing-scripts/week.py testing-data/test.csv "Baseline (From Memory)"
python3 graphing-scripts/exercise.py testing-data/test.csv "Mon - Pec Fly"
```