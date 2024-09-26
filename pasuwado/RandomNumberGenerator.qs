namespace RandomNumberGenerator {
    import Microsoft.Quantum.Convert.ResultArrayAsInt;
    import Microsoft.Quantum.Math.BitSizeI;

    operation GenerateRandomIntInRange(maximum : Int) : Int {
        mutable results = [];

        for _ in 1..BitSizeI(maximum) {
            set results += [GenerateRandomResult()]
        }

        let resultsAsInt = ResultArrayAsInt(results);

        return resultsAsInt > maximum ? GenerateRandomIntInRange(maximum) | resultsAsInt;
    }

    operation GenerateRandomResult() : Result {
        use qubit = Qubit();

        // Applies the Hadamard transformation to a single qubit.
        H(qubit);

        // Performs a measurement of a single qubit in the Pauli Z basis.
        let result = M(qubit);

        Reset(qubit);

        return result;
    }
}
