from bitstring import BitArray

class AES:
    def __init__(self) -> None:
        self.dataReset()

    def dataReset(self) -> None:
        self.data = {}

    def gs(self, v: BitArray) -> BitArray:
        pass

    def g(self, w: BitArray, rc: BitArray) -> BitArray:
        pass

    def transform(self, ki: BitArray) -> BitArray:
        pass
    
    def keySchedule(self, k: BitArray) -> list[BitArray]:
        kis = []
        ki = k
        roundLen = {
            128: 10,
            192: 12,
            256: 14,
        }
        for _ in range(roundLen[k.len]):
            ki = self.transform(ki)
            kis.append(ki)
        return kis

    def keyAddition(self, z: BitArray, ki: BitArray) -> BitArray:
        pass

    def byteSubstitution(self, z: BitArray) -> BitArray:
        pass

    def shiftRows(self, z: BitArray) -> BitArray:
        pass

    def mixColumns(self, z: BitArray) -> BitArray:
        pass

    def aesRound(self, z: BitArray) -> BitArray:
        pass

    def encrypt(self, x: BitArray, k: BitArray) -> BitArray:
        self.dataReset()
        self.data["x"] = x.hex
        self.data["k"] = k.hex
        kis = self.keySchedule(k)
        z = self.keyAddition(x)

    def decrypt(self, x: BitArray, k: BitArray) -> BitArray:
        self.dataReset()