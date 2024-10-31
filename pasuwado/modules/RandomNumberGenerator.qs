namespace RandomNumberGenerator {
    function ComputeNumberRepresentationInBits(number : Int) : Int {
        mutable number = number;
        mutable bits = 0;

        while (number != 0) {
            set bits = bits + 1;
            set number = number >>> 1;
        }

        bits
    }

    function SumResults(results : Result[]) : Int {
        let resultsLength = Length(results);

        mutable sum = 0;

        for resultIndex in 0..resultsLength - 1 {
            if (results[resultIndex] == One) {
                set sum |||= 1 <<< resultIndex;
            }
        }

        sum
    }

    operation Generate(maximum : Int) : Int {
        mutable results = [];

        for _ in 1..ComputeNumberRepresentationInBits(maximum) {
            use qubit = Qubit();

            // Applies the Hadamard transformation to a single qubit.
            H(qubit);

            // Performs a measurement of a single qubit in the Pauli Z basis.
            let result = M(qubit);

            Reset(qubit);

            set results += [result]
        }

        let resultsSum = SumResults(results);

        resultsSum > maximum ? Generate(maximum) | resultsSum
    }
}