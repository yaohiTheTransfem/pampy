fn sqrt(x: f64) -> f64 {
    let mut guess = x * 0.5;
    for _ite in 0..8 {
        guess = (guess + x / guess) * 0.5;
    }
    return guess;
}