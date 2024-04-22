htmlHeader = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>CoffeeBadgerPress</title>
        <meta name="viewport" content="width=device-width">
                <style>
            img {
                height: auto;
                display: block;
                margin-left: auto;
                margin-right: auto;
                max-width: 100%;
            }
            figure {
                max-width: fit-content;
            }
        @font-face {
        font-family: built;
        src: url(built\ titling\ sb.woff);
    }
    body{
        font-family: 'Times New Roman', Times, serif;
        font-weight: bold;
        font-size: 14px;
        color: #2f2f2f;
        background-color: rgb(252, 247, 225);
    }
    header{
        font-family: built;
        font-weight: 900;
        font-size: 80px;
        text-transform: uppercase;
        display: inline-block;
        line-height: 72px;
        
        letter-spacing: 8px;
        color:#5b5050;
    }

    p{
        margin-top: 0;
        margin-bottom: 20px;
    }
    .head{
        text-align: center;
        position: relative;
    }

    .title{
        text-align:center;
    }

    .subhead{
        text-transform: uppercase;
        border-bottom: 2px solid #2f2f2f;
        border-top: 2px solid #2f2f2f;
        padding: 12px 0 12px 0;

    }

    .content{
        font-size: 0;
        line-height: 0;
        word-spacing: -.31em;
        display: inline-block;
        margin: 30px 2% 0 2%;
        width: 96%;
    }
    
    .column{
        font-size: 14px;
        line-height: 20px;
        display: inline-block;
        vertical-align: top;
        margin-bottom: 50px;
        transition: all .7s;
        column-count: 3;
        column-rule-style:groove;
        height: auto;
        width: 100%;
    }

    .column + .column { 
    border-left: 0px solid #2f2f2f;
    }
    .column .headline{
        text-align: center;
        line-height: normal;
        font-family: 'Playfair Display', serif;
        display: block;
        margin: 0 auto;
    }

    .column .headline.hl3{
        font-weight: 400;
        font-style: italic;
        font-size: 36px;
        box-sizing: border-box;
        padding: 10px 0 10px 0;
    }
    .column .headline.hl4{
        font-weight: 700;
        font-size: 12px;
        box-sizing: border-box;
        padding: 10px 0 10px 0;
    }
    .column .headline.hl4:before{
        border-top: 5px solid #2f2f2f;
        content: '';
        width: 100px;
        height: 7px;
        display: block;
        margin: 0 auto;
    }
    .column .headline.hl4:after{
        border-bottom: 5px solid #2f2f2f;
        content: '';
        width: 100px;
        height: 10px;
        display: block;
        margin: 0 auto;
    }
   
    .column .figure {
        margin: 0 0 20px;
    }

    .wp-caption-text, .wp-element-caption {
        font-style: italic;
        font-size: 12px;
    }

    @media print {
        .content {
            display: block;
            break-before: auto;
        }
        .column { 
            display: block; 
            page-break-before: auto;
            page-break-after: always;
        }
    }

    </style>
    </head>
    """