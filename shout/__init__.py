import asyncio
import zmq
import zmq.asyncio
import csv

async def recv_transcriptions(socket):
    while True:
        transcription = await socket.recv_string()
        try:
            start, end, text = transcription.split('|')
        except ValueError:
            start = None
            end = None
            text = transcription.split('|')[-1]
        print("Received transcription:")
        print(start, end, text)

        with open('transcriptions.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
            csvwriter.writerow([start, end, text])

async def main():
    context = zmq.asyncio.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    print("Listening for transcriptions...")

    await recv_transcriptions(socket)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())