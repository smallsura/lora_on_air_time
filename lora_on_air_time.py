from math import ceil


def time_on_air(payload, sf, bandwidth=125, header=True, dr_opt=False,
                coding_rate=1):
    """
    Calculates time-on-air for LoRa messages
    @param payload: message being sent
    @param sf: spreading factor
    @param bandwidth: bandwidth in kHz
    @param header: presence of explicit header
    @param dr_opt: low DR optimise
    @param coding_rate: Error correction coding. 4/5 to 4/8 --> 1 to 4
    """

    # get payload size from payload
    payload_sz = len(payload)

    if header:
        H = 0
    else:
        H = 1

    if dr_opt:
        DE = 1
    else:
        DE = 0

    CR = 1  # 4/5-4/8 >> 1-4

    pre_sym = 8  # preamble symbols (8 standard for LoRaWAN)

    t_sym = (2 ** sf) / (bandwidth * 1000) * 1000

    t_pre = (pre_sym + 4.25) * t_sym

    payload_symb_nb = 8 + (max(ceil((8 * payload_sz - 4 * sf + 28 + 16 - 20
                                     * H) / (4 * (sf - 2 * DE))) *
                               (CR + 4), 0))

    t_pay = payload_symb_nb * t_sym

    t_packet = t_pre + t_pay

    return t_packet
