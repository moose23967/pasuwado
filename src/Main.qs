import Microsoft.Quantum.Convert.ResultArrayAsInt;
import Microsoft.Quantum.Convert.ResultArrayAsBoolArray;
import Microsoft.Quantum.Math.BitSizeI;

operation GeneratePassword(size : Int) : String {
    mutable password = "";
    let characters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"];

    for _ in 0..size-1 {
        set password += characters[ComplexRandom(Length(characters) - 1)];
    }

    return password;
}

operation ComplexRandom(max : Int) : Int {
    let maxAsBits = BitSizeI(max);

    mutable results = [];

    for _ in 1..maxAsBits {
        set results += [Random()]
    }

    let resultsAsInt = ResultArrayAsInt(results);

    return resultsAsInt > max ? ComplexRandom(max) | resultsAsInt;
}

operation Random() : Result {
    use qubit = Qubit();

    H(qubit);

    let result = M(qubit);

    Reset(qubit);

    return result;
}
