import math

"""
Thanks to stackoverflow

Eric Langlois (https://math.stackexchange.com/users/836999/eric-langlois)
How to find LCM of two numbers when one starts with an offset
URL (version: 2020-10-14): https://math.stackexchange.com/q/3864593
"""
def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.
    """
    gcd, s, t = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase

def extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def main():
    f = open('input.txt')

    goal = int(f.readline().strip())

    times = []
    stamps = []

    for i, t in enumerate(f.readline().strip().split(',')):
        if t != 'x':
            times.append(int(t))
            stamps.append(i)

    result = times[0]
    result_phase = 0

    for i in range(1, len(times)):
        #period, phase = combine_phased_rotations(result, result_phase, times[i], -stamps[i] % times[i])
        result, result_phase = combine_phased_rotations(result, result_phase, times[i], stamps[i])
        
        '''
        result = -phase % period - phase
        result_phase = phase
        '''

    print(-result_phase % result)

if __name__ == '__main__':
    main()