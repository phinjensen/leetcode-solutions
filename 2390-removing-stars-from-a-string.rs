impl Solution {
    pub fn remove_stars(s: String) -> String {
        let mut res = String::new();
        for c in s.chars() {
            if c == '*' {
                res.pop();
            } else {
                res.push(c);
            }
        }
        res
    }
}
