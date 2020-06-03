package com.example.diptam.dipbaazar;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;


public class MainActivity extends AppCompatActivity {

    private WebView mWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mWebView = (WebView) findViewById(R.id.activity_main_webview);
        WebSettings webSettings = mWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        mWebView.loadUrl("https://www.google.com/");
        mWebView.setWebViewClient(new com.example.diptam.dipbaazar.MyAppWebViewClient(){
            @Override
            public void onPageFinished(WebView view, String url) {
                //hide loading page
                findViewById(R.id.splashloading01).setVisibility(View.GONE);
                //show Webview
                findViewById(R.id.activity_main_webview).setVisibility((View.VISIBLE));
            }
        }
        );
    }

    @Override
    public void onBackPressed() {
        if (mWebView.canGoBack()) {
            mWebView.goBack();
        }
        else {
            super.onBackPressed();
        }
    }


    private class MyAppWebViewClient extends WebViewClient{

    }
}
