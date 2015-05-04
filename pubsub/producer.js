var kafka = require('kafka-node'),
    HighLevelProducer = kafka.HighLevelProducer,
    KeyedMessage = kafka.KeyedMessage;


function send (topic, message) {

    client = new kafka.Client('localhost:2181', 'jobSender');

    var producer = new HighLevelProducer(client),

    km = new KeyedMessage('key', 'message'),
    payloads = [
        { topic: topic, messages: message}
    ];

    producer.on('ready', function () {
      console.log("hi!");
      producer.send(payloads, function (err, data) {

        console.log("Data: " + JSON.stringify(data));

        if (err){
          console.log("Error sending " + data + "Error: " +err);
        }
        return(0);
      });
    });
}

send('test', 'testing custom sender!');
