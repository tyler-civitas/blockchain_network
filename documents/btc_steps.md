1. Built full bitcoin node on AWS.
Can control activity from outside using port 8333 (communication port for nodes)

2. Use linux distribution of bitcoind. Launch the bitcoin daemon service to run the node.
    Blockchain download began 06/08 at 5:30pm
    Ended at
    Total size

3. Chrontab to set service to begin when server is started

4. Check block count on internet to determine when block size is the same as the main blockchain.

5. Create ssh tunnel to interface with server and send remote procedure calls to port 8332 (requires localhost)

6. RPCs are sent in JSON format.
