# algorithms

A collection of 100 well-known algorithm and data-structure problems, the kind
commonly used for coding practice and technical interviews. Each problem has a
clear statement, worked examples, constraints, and a function signature, in a
simple JSON format that is easy to load into your own tools.

## Format

`problems.json` is the full index. Each problem is also available on its own at
`problems/<slug>.json`. Every problem looks like this:

```json
{
  "id": "1",
  "slug": "two-sum",
  "title": "Two Sum",
  "tags": ["Array", "Hash Table"],
  "statement": "…markdown description…",
  "functionName": "twoSum",
  "params": [{ "name": "nums", "type": "int[]" }, { "name": "target", "type": "int" }],
  "returns": "int[]",
  "examples": [{ "input": "…", "output": "…", "explanation": "…" }],
  "constraints": ["…"]
}
```

## License

MIT. See `LICENSE`.
