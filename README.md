# Fieldhouse Fantasy Demo

A small **educational Python project** showcasing fantasy scoring, simple projection rankings, and a start/sit comparison. Created as a public portfolio example alongside development of Fieldhouse Sports Intelligence.

**Not the production Fieldhouse prediction engine.** Uses illustrative sample projections, contains no live roster or injury feeds, and makes no claim to predict future player performance.

## Features
- Full-PPR receiving scoring (1 point per reception, 0.1 per receiving yard, 6 per receiving TD)
- Sort sample players by supplied projected fantasy points
- Recommend one of two players by supplied projections, including ties
- Unit tests for normal and edge cases

## Run
Requires Python 3.10+; no third-party packages.

```bash
python3 fantasy.py
python3 -m unittest discover -s tests -v
```

## Example
`ppr_points(7, 85, 2)` returns `27.5`.

## How it was built
This project was developed with AI assistance as a learning and portfolio exercise. I am practicing reading, testing, and explaining every component. All outputs are demonstrations, not real-time fantasy advice.

## Roadmap
- [ ] Add rushing and passing scoring rules
- [ ] Add optional league scoring settings
- [ ] Add CSV input validation
- [ ] Add GitHub Actions tests

## Responsible scope
No API keys, proprietary formulas, customer data, or private Fieldhouse production code are included.
