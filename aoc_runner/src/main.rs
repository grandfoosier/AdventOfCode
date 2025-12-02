use std::env;
use std::fs;
use std::path::PathBuf;

mod generated_mods;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut args = env::args().skip(1);
    let year = args.next().unwrap_or_else(|| "2025".to_string());
    let day_arg = args.next().unwrap_or_else(|| "1".to_string());

    // Normalize day to two digits when possible
    let day_padded = match day_arg.parse::<u32>() {
        Ok(n) => format!("{:02}", n),
        Err(_) => day_arg.clone(),
    };

    // Build path: <repo-root>/<year>/inputs/<DD>.txt
    // `CARGO_MANIFEST_DIR` points to the `aoc_runner` folder; go one level up to the repository root.
    let manifest_dir = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    let repo_root = match manifest_dir.join("..").canonicalize() {
        Ok(p) => p,
        Err(_) => manifest_dir.clone(),
    };

    let input_path = repo_root.join(&year).join("inputs").join(format!("{}.txt", day_padded));

    // If the input file is missing, fall back to empty input.
    let input = match fs::read_to_string(&input_path) {
        Ok(s) => s,
        Err(e) => {
            if e.kind() == std::io::ErrorKind::NotFound {
                //eprintln!("Input file not found at '{}', using empty input.", input_path.display());
                String::new()
            } else {
                return Err(Box::new(e));
            }
        }
    };

    generated_mods::dispatch(&year, &day_padded, &input).map_err(|e| format!("{}", e))?;

    Ok(())
}
