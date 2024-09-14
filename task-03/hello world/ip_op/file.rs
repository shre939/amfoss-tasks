use std::fs;

fn main() -> std::io::Result<()> {
    let content = fs::read_to_string("input.txt")?;
    fs::write("output.txt", content)?;
    Ok(())
}
