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

    let input_path = input_path.canonicalize().map_err(|e| {
        format!(
            "Failed to locate input file '{}': {}. (manifest_dir='{}', attempted='{}')",
            input_path.display(), e, manifest_dir.display(), repo_root.display()
        )
    })?;
    let input = fs::read_to_string(&input_path)?;

    generated_mods::dispatch(&year, &day_padded, &input).map_err(|e| format!("{}", e))?;

    Ok(())
}
