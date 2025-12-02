# AoC Runner

Small runner to call solution functions placed under `<year>/solutions/<DD>.rs` using the input file at `<year>/inputs/<DD>.txt`.

Usage (from repository root):

PowerShell:
```
cd c:\Users\rices\Documents\AdventOfCode\aoc_runner
cargo run -- 2025 1
```

This will read `2025/inputs/01.txt` and call the `run(input: &str)` function found in `2025/solutions/01.rs`.

Notes:
- Add more `pub mod dayXX { include!(...) }` entries in `src/main.rs` to include additional days' solution files.
- Solution files must define `pub fn run(input: &str)`.
