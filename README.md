stock_ai_agent/
│
├── data/
│   ├── raw/
│   │   ├── zerodha_basics.pdf
│   │   ├── zerodha_fundamental.pdf
│   │   └── structured_txt/
│   │       ├── ratios.txt
│   │       ├── macro.txt
│   │       ├── risk.txt
│   │       └── portfolio.txt
│   │
│   └── processed/
│
├── src/
│   ├── loaders/
│   │   ├── pdf_loader.py
│   │   └── txt_loader.py
│   │
│   ├── processing/
│   │   ├── cleaner.py
│   │   ├── chunker.py
│   │   └── formatter.py
│   │
│   ├── embeddings/
│   │   └── embedder.py
│   │
│   ├── vectordb/
│   │   └── db.py
│   │
│   ├── retrieval/
│   │   └── retriever.py
│   │
│   ├── agent/
│   │   ├── prompt.py
│   │   └── agent.py
│   │
│   └── main.py
│
├── requirements.txt
└── .env