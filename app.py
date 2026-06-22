import gradio as gr
import joblib

# Load model
pipeline = joblib.load("tweeteval_pipeline.joblib")

def predict_sentiment(text):
    if not text.strip():
        return "❗ Please enter a tweet."
    
    prediction = pipeline.predict([text])[0]

    # Convert prediction to labels + emojis
    if prediction == 1:
        return "😊 **Positive Tweet**"
    elif prediction == 0:
        return "😡 **Negative Tweet**"
    else:
        return f"🔍 Sentiment: {prediction}"

# ---------------------------- UI DESIGN ---------------------------- #

with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue", secondary_hue="pink")) as demo:
    
    # Header
    gr.Markdown(
        """
        <h1 style="text-align:center; color:#4A90E2; font-size:38px;">
            💬 SocialPulse - Tweet Sentiment Analyzer
        </h1>

        <p style="text-align:center; font-size:18px; color:#333;">
            Analyze the sentiment of any tweet using Machine Learning.<br>
        </p>

        <hr>
        """
    )

    with gr.Row():
        with gr.Column(scale=2):

            tweet_input = gr.Textbox(
                label="✍️ Enter Tweet",
                placeholder="Type a tweet here...",
                lines=3
            )

            analyze_btn = gr.Button(
                "🔍 Analyze Sentiment",
                variant="primary"
            )

        with gr.Column(scale=1):

            output_box = gr.Markdown(
                "<div style='font-size:22px; color:#444;'>Sentiment will appear here...</div>"
            )

    analyze_btn.click(
        fn=predict_sentiment,
        inputs=tweet_input,
        outputs=output_box
    )

    # Footer
    gr.Markdown(
        """
        <hr>
        <p style="text-align:center; font-size:15px; color:gray;">
            🚀 Developed by Shivangini Gupta
        </p>
        """
    )

demo.launch(share=True)
