import deepcodec

deepcodec.logging.set_level(deepcodec.logging.VERBOSE)

input_file = deepcodec.open("input.wav")
output_file = deepcodec.open("output.wav", mode="w")

input_stream = input_file.streams.audio[0]
output_stream = output_file.add_stream("pcm_s16le", rate=input_stream.rate)

graph = deepcodec.filter.Graph()
graph.link_nodes(
    graph.add_abuffer(template=input_stream),
    graph.add("atempo", "2.0"),
    graph.add("abuffersink"),
).configure()

for frame in input_file.decode(input_stream):
    graph.push(frame)
    while True:
        try:
            for packet in output_stream.encode(graph.pull()):
                output_file.mux(packet)
        except (deepcodec.BlockingIOError, deepcodec.EOFError):
            break

# Flush the stream
for packet in output_stream.encode(None):
    output_file.mux(packet)

input_file.close()
output_file.close()
