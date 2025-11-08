'''
Realizar un programa en el lenguaje de su preferencia, que reciba como parámetros el
tamaño total del mensaje IPv4 de entrada, la longitud del header del mismo, el MTU de salida y el bit
dont fragment y muestre cómo resultaría la fragmentación del mismo. Por ejemplo un datagrama de
1100B con un header de 20B (mínimo) y un MTU de salida de 200:

show_frag(1100,20,200,0)

1080 TotalDataSent= 176 packetPayloadLength=176 OffsetBytes=   0 SentOffset=  0 DF=0 MF=1 
 904 TotalDataSent= 352 packetPayloadLength=176 OffsetBytes= 176 SentOffset= 22 DF=0 MF=1
 728 TotalDataSent= 528 packetPayloadLength=176 OffsetBytes= 352 SentOffset= 44 DF=0 MF=1
 552 TotalDataSent= 704 packetPayloadLength=176 OffsetBytes= 528 SentOffset= 66 DF=0 MF=1
 376 TotalDataSent= 880 packetPayloadLength=176 OffsetBytes= 704 SentOffset= 88 DF=0 MF=1
 200 TotalDataSent=1056 packetPayloadLength=176 OffsetBytes= 880 SentOffset=110 DF=0 MF=1
  24 TotalDataSent=1080 packetPayloadLength= 24 OffsetBytes=1056 SentOffset=132 DF=0 MF=0

Fragments=7 TotalBytesIN/OUT=1100/1220
'''

def show_frag(total_size, header_length, mtu, dont_fragment):
    data_size = total_size - header_length
    max_payload = (mtu - header_length) // 8 * 8
    remaining_data = data_size
    offset = 0
    fragments = []
    total_bytes_out = 0
    total_data_sent = 0
    
    while remaining_data > 0:
        if dont_fragment and remaining_data > max_payload:
            print("Fragmentation not allowed due to DF bit set.")
            return

        if remaining_data > max_payload:
            payload_length = max_payload
            more_fragments = 1
        else:
            payload_length = remaining_data
            if payload_length > 8:
                payload_length = (payload_length // 8) * 8
            more_fragments = 1 if remaining_data > payload_length else 0

        total_data_sent += payload_length
        fragment_total_size = remaining_data
        fragments.append((fragment_total_size, total_data_sent, payload_length, offset, offset // 8, dont_fragment, more_fragments))
        total_bytes_out += (payload_length + header_length)

        remaining_data -= payload_length
        offset += payload_length
    for frag in fragments:
        print(f"{frag[0]:4d} TotalDataSent={frag[1]:4d} packetPayloadLength={frag[2]:3d} OffsetBytes={frag[3]:4d} SentOffset={frag[4]:3d} DF={frag[5]} MF={frag[6]}")
    print(f"\nFragments={len(fragments)} TotalBytesIN/OUT={total_size}/{total_bytes_out}")

show_frag(1100, 20, 200, 0)