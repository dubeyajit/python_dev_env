from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("Name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("Views", type=int, help="Views of the video")
video_put_args.add_argument("Likes", type=int, help="Likes on the video")

videos = {}
names = {"Ajit": {"Age":49, "Gender":"Male"},
         "Sheela": {"Age":49, "Gender":"Female"}
}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video")

class HelloWorld(Resource):
    def get(self,name):
        return names[name]

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201


api.add_resource(HelloWorld, "/helloworld/<string:name>/")
api.add_resource(Video, "/video/<int:video_id>")


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)