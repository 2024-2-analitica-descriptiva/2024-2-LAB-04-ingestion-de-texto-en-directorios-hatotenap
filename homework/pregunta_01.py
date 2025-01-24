# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    import os
    import zipfile
    import pandas as pd

    # Paths
    input_zip_path = 'files/input.zip' 
    output_dir = 'files/output/'  
    input_extracted_path = 'files/input/' 

    
    os.makedirs(output_dir, exist_ok=True)

    
    if os.path.exists(input_extracted_path):
       
        import shutil
        shutil.rmtree(input_extracted_path)
    os.makedirs(input_extracted_path, exist_ok=True)

    with zipfile.ZipFile(input_zip_path, 'r') as zip_ref:
        zip_ref.extractall(input_extracted_path)

   
    datasets = ['train', 'test']  
    columns = ['phrase', 'target']  

    generated_files = []

    for dataset in datasets:
        data_dir = os.path.join(input_extracted_path, 'input', dataset)
        rows = []

        for sentiment in ['positive', 'negative', 'neutral']:
            sentiment_dir = os.path.join(data_dir, sentiment)
            for file_name in os.listdir(sentiment_dir):
                file_path = os.path.join(sentiment_dir, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    phrase = file.read().strip()
                    rows.append({'phrase': phrase, 'target': sentiment})

        df = pd.DataFrame(rows, columns=columns)
        output_file_path = os.path.join(output_dir, f"{dataset}_dataset.csv")
        df.to_csv(output_file_path, index=False)
        generated_files.append(output_file_path)

    return generated_files
