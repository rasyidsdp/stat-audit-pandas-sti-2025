import numpy as np
import random
import math

# =====================================================================
# BAGIAN 1: ESTIMATE PROBABILITY
# =====================================================================

def estimate_probability(event_fn, n_trials=50000):
    """
    Mengestimasi probabilitas suatu kejadian menggunakan metode Monte Carlo.
    
    :param event_fn: Fungsi yang mengembalikan True jika kejadian terjadi, False jika tidak.
    :param n_trials: Jumlah simulasi yang dijalankan.
    :return: Estimasi probabilitas (float).
    """
    successes = 0
    for _ in range(n_trials):
        if event_fn():
            successes += 1
            
    return successes / n_trials


# =====================================================================
# BAGIAN 2: BLOOM FILTER
# =====================================================================

class BloomFilter:
    def __init__(self, m, k):
        """
        Inisialisasi Bloom Filter.
        
        :param m: Ukuran bit array (size of bit array)
        :param k: Jumlah fungsi hash (number of hash functions)
        """
        self.m = m
        self.k = k
        self.bit_array = [0] * m

    def _hashes(self, item):
        """
        Fungsi internal untuk menghasilkan k indeks hash yang berbeda 
        menggunakan trik salting berbasis bawaan hash() Python.
        """
        indices = []
        for i in range(self.k):
            # Menggunakan string unique salt untuk setiap fungsi hash
            hash_val = hash(f"{item}-{i}")
            indices.append(hash_val % self.m)
        return indices

    def add(self, item):
        """Menambahkan elemen ke dalam Bloom Filter."""
        for index in self._hashes(item):
            self.bit_array[index] = 1

    def contains(self, item):
        """
        Memeriksa apakah elemen *mungkin* ada di dalam Bloom Filter.
        """
        for index in self._hashes(item):
            if self.bit_array[index] == 0:
                return False  # Pasti belum pernah ditambahkan
        return True  # Mungkin sudah ditambahkan (bisa False Positive)

    def theoretical_fpr(self, n):
        """
        Menghitung nilai False Positive Rate (FPR) secara teoritis.
        
        Formula: (1 - e^(-k * n / m))^k
        :param n: Jumlah elemen yang telah dimasukkan ke dalam filter
        """
        if self.m == 0:
            return 1.0
        exponent = - (self.k * n) / self.m
        base = 1 - math.exp(exponent)
        return math.pow(base, self.k)


# =====================================================================
# BAGIAN 3: MCMC KNAPSACK
# =====================================================================

def mcmc_knapsack(items, capacity, n_iter=100000):
    """
    Menyelesaikan Knapsack Problem menggunakan Algoritma Metropolis-Hastings (MCMC).
    
    :param items: List of dict, contoh: [{'weight': 10, 'value': 60}, ...]
    :param capacity: Kapasitas berat maksimum knapsack
    :param n_iter: Jumlah iterasi MCMC
    :return: (best_state, best_value)
    """
    num_items = len(items)
    
    # State awal: semua barang tidak diambil (0)
    current_state = np.zeros(num_items, dtype=int)
    current_value = 0
    current_weight = 0
    
    best_state = current_state.copy()
    best_value = current_value

    for _ in range(n_iter):
        # 1. Pilih satu item secara acak untuk diubah statusnya (0 jadi 1, atau 1 jadi 0)
        proposal_idx = random.randint(0, num_items - 1)
        proposal_state = current_state.copy()
        proposal_state[proposal_idx] = 1 - proposal_state[proposal_idx] # Flip bit
        
        # 2. Hitung berat dan nilai dari proposal state
        proposal_weight = sum(proposal_state[i] * items[i]['weight'] for i in range(num_items))
        proposal_value = sum(proposal_state[i] * items[i]['value'] for i in range(num_items))
        
        # 3. Validasi batasan kapasitas
        if proposal_weight > capacity:
            # Jika melebihi kapasitas, berikan penalti berat pada nilainya 
            # atau langsung tolak (di sini kita beri peluang sangat kecil/penalti)
            proposal_value = 0 
            
        # 4. Kriteria Penerimaan Metropolis-Hastings
        # Jika nilai proposal lebih baik, langsung terima. 
        # Jika lebih buruk, terima dengan probabilitas exp(proposal_val - current_val)
        if proposal_value > current_value:
            accept = True
        else:
            # Menggunakan basis eksponensial sederhana untuk eksplorasi
            prob = math.exp(proposal_value - current_value) if proposal_value > 0 else 0
            accept = random.random() < prob
            
        if accept:
            current_state = proposal_state
            current_value = proposal_value
            current_weight = proposal_weight
            
            # Simpan jika ini adalah kombinasi terbaik yang pernah ditemukan
            if current_value > best_value and current_weight <= capacity:
                best_value = current_value
                best_state = current_state.copy()
                
    return best_state, best_value