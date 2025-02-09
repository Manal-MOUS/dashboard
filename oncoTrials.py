###########################################################################################################################################
import dash_bootstrap_components as dbc
import dash
from dash import dash_table, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
###########################################################################################################################################
mesh_dict = {
'Neoplasms by Site': ['Abdominal Neoplasms', 'Unilateral Breast Neoplasms',
'Colitis-Associated Neoplasms', 'Cardiac Papillary Fibroelastoma', 'Adrenal Cortex Neoplasms',
'Adrenal Gland Neoplasms', 'Anal Gland Neoplasms', 'Anus Neoplasms', 'Appendiceal Neoplasms',
'Bile Duct Neoplasms', 'Biliary Tract Neoplasms', 'Urinary Bladder Neoplasms', 'Bone Neoplasms', 'Brain Neoplasms',
'Breast Neoplasms', 'Bronchial Neoplasms', 'Carcinoma, Bronchogenic', 'Carcinoma, Non-Small-Cell Lung', 'Cecal Neoplasms',
'Cerebellar Neoplasms', 'Cerebral Ventricle Neoplasms', 'Uterine Cervical Neoplasms', 'Choroid Neoplasms',
'Colonic Neoplasms', 'Colorectal Neoplasms, Hereditary Nonpolyposis', 'Common Bile Duct Neoplasms', 'Conjunctival Neoplasms',
'Cranial Nerve Neoplasms', 'Digestive System Neoplasms', 'Duodenal Neoplasms', 'Ear Neoplasms', 'Endocrine Gland Neoplasms',
'Esophageal Neoplasms', 'Eye Neoplasms', 'Eyelid Neoplasms', 'Facial Neoplasms', 'Fallopian Tube Neoplasms', 'Femoral Neoplasms',
'Gallbladder Neoplasms', 'Gastrointestinal Neoplasms', 'Genital Neoplasms, Female', 'Genital Neoplasms, Male', 'Gingival Neoplasms',
'Head and Neck Neoplasms', 'Heart Neoplasms', 'Hypopharyngeal Neoplasms', 'Hypothalamic Neoplasms', 'Ileal Neoplasms', 'Intestinal Neoplasms',
'Jaw Neoplasms', 'Jejunal Neoplasms', 'Kidney Neoplasms', 'Laryngeal Neoplasms', 'Leukoplakia, Oral', 'Lip Neoplasms', 'Liver Neoplasms',
'Liver Neoplasms, Experimental', 'Lung Neoplasms', 'Mammary Neoplasms, Experimental', 'Mandibular Neoplasms', 'Maxillary Neoplasms',
'Maxillary Sinus Neoplasms', 'Mediastinal Neoplasms', 'Meigs Syndrome', 'Meningeal Neoplasms', 'Mouth Neoplasms', 'Myasthenia Gravis', 'Myelitis, Transverse',
'Nasopharyngeal Neoplasms', 'Nelson Syndrome', 'Neoplasms by Site', 'Multiple Endocrine Neoplasia', 'Paraneoplastic Endocrine Syndromes', 'Nervous System Neoplasms',
'Nose Neoplasms', 'Orbital Neoplasms', 'Oropharyngeal Neoplasms', 'Otorhinolaryngologic Neoplasms', 'Ovarian Neoplasms', 'Palatal Neoplasms', 'Pancoast Syndrome',
'Pancreatic Neoplasms', 'Paranasal Sinus Neoplasms', 'Parathyroid Neoplasms', 'Parotid Neoplasms', 'Pelvic Neoplasms', 'Penile Neoplasms',
'Peripheral Nervous System Neoplasms', 'Peritoneal Neoplasms', 'Pharyngeal Neoplasms', 'Pituitary Neoplasms', 'Pleural Neoplasms', 'Polycythemia Vera',
'Prostatic Neoplasms', 'Rectal Neoplasms', 'Respiratory Tract Neoplasms', 'Retroperitoneal Neoplasms', 'Salivary Gland Neoplasms', 'Sebaceous Gland Neoplasms',
'Sigmoid Neoplasms', 'Skin Neoplasms', 'Skull Neoplasms', 'Soft Tissue Neoplasms', 'Spinal Cord Neoplasms', 'Spinal Neoplasms', 'Splenic Neoplasms', 'Stomach Neoplasms',
'Sublingual Gland Neoplasms', 'Submandibular Gland Neoplasms', 'Sweat Gland Neoplasms', 'Testicular Neoplasms', 'Thoracic Neoplasms', 'Thymus Neoplasms',
'Thyroid Neoplasms', 'Tongue Neoplasms', 'Tonsillar Neoplasms', 'Tracheal Neoplasms', 'Ureteral Neoplasms', 'Urethral Neoplasms', 'Urogenital Neoplasms',
'Urologic Neoplasms', 'Uterine Neoplasms', 'Uveal Neoplasms', 'Vaginal Neoplasms', 'Venereal Tumors, Veterinary', 'Vulvar Neoplasms', 'Supratentorial Neoplasms',
'Epidural Neoplasms', 'Colorectal Neoplasms', 'Infratentorial Neoplasms', 'Lambert-Eaton Myasthenic Syndrome', 'Mammary Neoplasms, Animal', 'Iris Neoplasms',
'Pleural Effusion, Malignant', 'Central Nervous System Neoplasms', 'Choroid Plexus Neoplasms', 'Thyroid Nodule', 'Endometrial Neoplasms', 'Leukoplakia, Hairy',
'Adrenocortical Adenoma', 'Breast Neoplasms, Male', 'Multiple Endocrine Neoplasia Type 1', 'Multiple Endocrine Neoplasia Type 2a',
'Multiple Endocrine Neoplasia Type 2b', 'Muscle Neoplasms', 'Vascular Neoplasms', 'Bone Marrow Neoplasms', 'Skull Base Neoplasms', 'Hematologic Neoplasms',
'Retinal Neoplasms', 'Optic Nerve Neoplasms', 'Papilloma, Choroid Plexus', 'Brain Stem Neoplasms', 'Paraneoplastic Syndromes, Nervous System',
'Paraneoplastic Cerebellar Degeneration', 'Limbic Encephalitis', 'Paraneoplastic Polyneuropathy', 'Central Nervous System Cysts', 'Pulmonary Sclerosing Hemangioma',
'Adamantinoma', 'Opsoclonus-Myoclonus Syndrome', 'Multiple Pulmonary Nodules', 'Muir-Torre Syndrome', 'Small Cell Lung Carcinoma', 'Meningeal Carcinomatosis',
"Sister Mary Joseph's Nodule", 'Inflammatory Breast Neoplasms', 'Paraneoplastic Syndromes, Ocular', 'Anti-N-Methyl-D-Aspartate Receptor Encephalitis',
'Hereditary Breast and Ovarian Cancer Syndrome', 'Prostatic Neoplasms, Castration-Resistant', 'Triple Negative Breast Neoplasms'],
'Neoplasms by Histologic Type': ['Plasmablastic Lymphoma', 'Mammary Analogue Secretory Carcinoma', 'Giant Cell Tumor of Tendon Sheath',
'Fibromatosis, Plantar', 'Breast Carcinoma In Situ', 'Tubular Sweat Gland Adenomas', 'Immunoglobulin Light-chain Amyloidosis', 'Adenocarcinoma of Lung',
'Squamous Cell Carcinoma of Head and Neck', 'Chondrosarcoma, Clear Cell', 'Carcinoma, Ovarian Epithelial', 'Thyroid Cancer, Papillary', 'Nasopharyngeal Carcinoma',
'Esophageal Squamous Cell Carcinoma', 'Myopericytoma', 'Pancreatic Intraductal Neoplasms', 'Diffuse Intrinsic Pontine Glioma', 'Mesothelioma, Malignant',
'Non-Muscle Invasive Bladder Neoplasms', 'Melanoma, Cutaneous Malignant', 'Adenocarcinoma', 'Adenocarcinoma, Papillary', 'Adenofibroma', 'Adenolymphoma',
'Adenoma', 'Adenoma, Basophil', 'Adenoma, Chromophobe', 'Adenoma, Acidophil', 'Adrenal Rest Tumor', 'Ameloblastoma', 'Angiokeratoma', 'Apudoma', 'Astrocytoma',
'Avian Leukosis', 'Sarcoma, Avian', 'Blast Crisis', "Bowen's Disease", 'Brenner Tumor', 'Burkitt Lymphoma', 'Carcinoid Heart Disease', 'Carcinoid Tumor', 'Carcinoma',
'Carcinoma in Situ', 'Carcinoma 256, Walker', 'Carcinoma, Basal Cell', 'Carcinoma, Basosquamous', 'Adenocarcinoma, Bronchiolo-Alveolar',
'Carcinoma, Intraductal, Noninfiltrating', 'Carcinoma, Ehrlich Tumor', 'Carcinoma, Krebs 2', 'Adenocarcinoma, Mucinous', 'Carcinoma, Papillary',
'Carcinoma, Renal Cell', 'Adenocarcinoma, Scirrhous', 'Carcinoma, Squamous Cell', 'Carcinoma, Transitional Cell', 'Carcinosarcoma', 'Carotid Body Tumor',
'Cementoma', 'Adenoma, Bile Duct', 'Chondroblastoma', 'Chondroma', 'Chondrosarcoma', 'Chordoma', 'Hydatidiform Mole, Invasive', 'Choriocarcinoma', 'Craniopharyngioma',
'Carcinoma, Adenoid Cystic', 'Cystadenocarcinoma', 'Cystadenoma', 'Phyllodes Tumor', 'Vipoma', 'Dupuytren Contracture', 'Dysgerminoma', 'Dysplastic Nevus Syndrome',
'Ependymoma', 'Leukemia, Erythroblastic, Acute', 'Exostoses, Multiple Hereditary', 'Fibroma', 'Fibrosarcoma', 'Ganglioneuroma', 'Gardner Syndrome',
'Giant Cell Tumors', 'Glioblastoma', 'Glioma', 'Glomus Tumor', 'Glomus Jugulare Tumor', 'Glucagonoma', 'Granulosa Cell Tumor', 'Hemangioendothelioma',
'Hemangioma', 'Hemangioma, Cavernous', 'Hemangiopericytoma', 'Hemangiosarcoma', 'Carcinoma, Hepatocellular', 'Adenoma, Sweat Gland', 'Hodgkin Disease',
'Hydatidiform Mole', 'Immunoproliferative Small Intestinal Disease', 'Insulinoma', 'Adenoma, Islet Cell', 'Krukenberg Tumor', 'Leiomyoma', 'Leiomyosarcoma',
'Leukemia', 'Leukemia L1210', 'Leukemia L5178', 'Leukemia P388', 'Leukemia, Experimental', 'Leukemia, Hairy Cell', 'Leukemia, Lymphoid', 'Leukemia, Mast-Cell',
'Leukemia, Megakaryoblastic, Acute', 'Leukemia, Monocytic, Acute', 'Leukemia, Myeloid', 'Leukemia, Plasma Cell', 'Leukemia, Radiation-Induced', 'Leydig Cell Tumor',
'Linitis Plastica', 'Lipoma', 'Liposarcoma', 'Lymphangioma', 'Lymphangiomyoma', 'Lymphangiosarcoma', 'Lymphoma', 'Lymphoma, Follicular', 'Lymphoma, Non-Hodgkin',
'Lymphomatoid Granulomatosis', 'Waldenstrom Macroglobulinemia', 'Malignant Carcinoid Syndrome', 'Mastocytosis', 'Medulloblastoma', 'Melanoma', 'Melanoma, Experimental',
'Meningioma', 'Mesenchymoma', 'Mesonephroma', 'Mesothelioma', 'Adenoma, Pleomorphic', 'Multiple Myeloma', 'Mycosis Fungoides', 'Myoepithelioma', 'Myoma', 'Myosarcoma',
'Myxoma', 'Myxosarcoma', 'Neoplasms by Histologic Type', 'Neoplasms, Connective Tissue', 'Neoplasms, Germ Cell and Embryonal',
'Neoplasms, Glandular and Epithelial', 'Neoplasms, Muscle Tissue', 'Neoplasms, Nerve Tissue', 'Neoplasms, Vascular Tissue', 'Wilms Tumor', 'Neurilemmoma',
'Neuroblastoma', 'Neurofibroma', 'Neurofibromatosis 1', 'Neuroma', 'Neuroma, Acoustic', 'Nevus', 'Nevus of Ota', 'Nevus, Pigmented', 'Odontogenic Tumors', 'Odontoma',
'Oligodendroglioma', 'Osteoma', 'Osteoma, Osteoid', "Paget's Disease, Mammary", 'Paget Disease, Extramammary', 'Papilloma', 'Paraganglioma',
'Paraganglioma, Extra-Adrenal', 'Pheochromocytoma', 'Pinealoma', 'Plasmacytoma', 'Adenomatous Polyposis Coli', 'Pseudomyxoma Peritonei', 'Pulmonary Adenomatosis, Ovine',
'Retinoblastoma', 'Rhabdomyoma', 'Rhabdomyosarcoma', 'Sarcoma', 'Sarcoma 180', 'Sarcoma 37', 'Sarcoma, Ewing', 'Sarcoma, Experimental',
'Sarcoma, Kaposi', 'Mast-Cell Sarcoma', 'Osteosarcoma', 'Sarcoma, Yoshida', 'Sertoli Cell Tumor', 'Sezary Syndrome', 'Somatostatinoma', 'Struma Ovarii',
'Sturge-Weber Syndrome', 'Sarcoma, Synovial', 'Synovitis, Pigmented Villonodular', 'Teratoma', 'Thecoma', 'Thymoma', 'Trophoblastic Neoplasms', 'Urticaria Pigmentosa',
'Prolactinoma', 'Carcinoma, Merkel Cell', 'Gastrinoma', 'Leukemia, B-Cell', 'Leukemia, Lymphocytic, Chronic, B-Cell', 'Precursor B-Cell Lymphoblastic Leukemia-Lymphoma',
'Leukemia, Biphenotypic, Acute', 'Leukemia, T-Cell', 'Leukemia-Lymphoma, Adult T-Cell', 'Leukemia, Prolymphocytic, T-Cell', 'Leukemia, Prolymphocytic',
'Leukemia, Myelogenous, Chronic, BCR-ABL Positive', 'Leukemia, Myeloid, Accelerated Phase', 'Leukemia, Myeloid, Chronic-Phase', 'Leukemia, Myeloid, Acute',
'Leukemia, Basophilic, Acute', 'Leukemia, Eosinophilic, Acute', 'Leukemia, Promyelocytic, Acute', 'Leukemia, Myelomonocytic, Chronic', 'Leukemia, Myelomonocytic, Acute',
'Histiocytic Disorders, Malignant', 'Osteochondroma', 'Lymphoma, B-Cell', 'Lymphoma, T-Cell', 'Lymphoma, Large-Cell, Immunoblastic', 'Lymphoma, Large B-Cell, Diffuse',
'Lymphoma, T-Cell, Cutaneous', 'Lymphoma, T-Cell, Peripheral', 'Lymphoma, AIDS-Related', 'Neurofibromatosis 2', 'Leukemia, Feline', 'Enzootic Bovine Leukosis',
'Granular Cell Tumor', 'Neurofibromatoses', 'Neuroectodermal Tumors', 'Neuroectodermal Tumor, Melanotic', 'WAGR Syndrome', 'Lymphoma, Large-Cell, Anaplastic',
'Lymphomatoid Papulosis', 'Lymphatic Vessel Tumors', 'Lymphangioma, Cystic', 'Lymphangioleiomyomatosis', 'Neoplasms, Complex and Mixed', 'Adenomyoma', 'Adenosarcoma',
'Carcinoma, Adenosquamous', 'Hepatoblastoma', 'Mixed Tumor, Malignant', 'Mixed Tumor, Mesodermal', 'Mixed Tumor, Mullerian', 'Nephroma, Mesoblastic',
'Pulmonary Blastoma', 'Sarcoma, Endometrial Stromal', 'Neoplasms, Connective and Soft Tissue', 'Neoplasms, Adipose Tissue', 'Angiolipoma', 'Angiomyolipoma',
'Liposarcoma, Myxoid', 'Myelolipoma', 'Chondromatosis', 'Chondrosarcoma, Mesenchymal', 'Giant Cell Tumor of Bone', 'Neoplasms, Bone Tissue', 'Fibroma, Ossifying',
'Osteoblastoma', 'Osteochondromatosis', 'Osteosarcoma, Juxtacortical', 'Neoplasms, Fibrous Tissue', 'Histiocytoma, Benign Fibrous', 'Fibroma, Desmoplastic',
'Fibromatosis, Abdominal', 'Fibromatosis, Aggressive', 'Dermatofibrosarcoma', 'Myofibromatosis', 'Neoplasms, Fibroepithelial', 'Fibroadenoma', 'Sarcoma, Clear Cell',
'Sarcoma, Small Cell', 'Angiomyoma', 'Leiomyoma, Epithelioid', 'Leiomyomatosis', 'Rhabdomyosarcoma, Alveolar', 'Rhabdomyosarcoma, Embryonal',
'Sarcoma, Alveolar Soft Part', 'Smooth Muscle Tumor', 'Carcinoma, Embryonal', 'Germinoma', 'Gonadoblastoma', 'Seminoma', 'Endodermal Sinus Tumor',
'Neuroectodermal Tumors, Primitive, Peripheral', 'Neuroectodermal Tumors, Primitive', 'Teratocarcinoma', 'Trophoblastic Tumor, Placental Site', 'Adenoma, Liver Cell',
'Adenoma, Oxyphilic', 'Acrospiroma', 'Hidrocystoma', 'Syringoma', 'Adenoma, Villous', 'Adenomatoid Tumor', 'Adenomatosis, Pulmonary', 'Adenomatous Polyps',
'Mesothelioma, Cystic', 'Adenocarcinoma, Clear Cell', 'Adenocarcinoma, Follicular', 'Carcinoma, Papillary, Follicular', 'Adenocarcinoma, Sebaceous',
'Carcinoma, Acinar Cell', 'Adrenocortical Carcinoma', 'Carcinoma, Endometrioid', 'Carcinoma, Ductal, Breast', 'Carcinoma, Islet Cell', 'Carcinoma, Lobular',
'Carcinoma, Medullary', 'Carcinoma, Mucoepidermoid', 'Carcinoma, Neuroendocrine', 'Carcinoma, Signet Ring Cell', 'Carcinoma, Skin Appendage', 'Cholangiocarcinoma',
'Cystadenocarcinoma, Mucinous', 'Cystadenocarcinoma, Papillary', 'Cystadenocarcinoma, Serous', 'Klatskin Tumor', 'Carcinoma, Giant Cell', 'Carcinoma, Large Cell',
'Carcinoma, Small Cell', 'Carcinoma, Verrucous', 'Cystadenoma, Mucinous', 'Cystadenoma, Papillary', 'Cystadenoma, Serous', 'Neoplasms, Adnexal and Skin Appendage',
'Neoplasms, Basal Cell', 'Pilomatrixoma', 'Neoplasms, Cystic, Mucinous, and Serous', 'Mucoepidermoid Tumor', 'Neoplasms, Ductal, Lobular, and Medullary',
'Papilloma, Intraductal', 'Neoplasms, Mesothelial', 'Neoplasms, Neuroepithelial', 'Ganglioglioma', 'Esthesioneuroblastoma, Olfactory', 'Ganglioneuroblastoma',
'Neurocytoma', 'Neoplasms, Squamous Cell', 'Papilloma, Inverted', 'Neoplasms, Gonadal Tissue', 'Sertoli-Leydig Cell Tumor', 'Luteoma', 'Sex Cord-Gonadal Stromal Tumors',
'Glioma, Subependymal', 'Gliosarcoma', 'Nerve Sheath Neoplasms', 'Neurofibroma, Plexiform', 'Neurofibrosarcoma', 'Neurothekeoma', 'Angiofibroma',
'Hemangioendothelioma, Epithelioid', 'Hemangioma, Capillary', 'Hemangioblastoma', 'Nevi and Melanomas', "Hutchinson's Melanotic Freckle", 'Melanoma, Amelanotic',
'Nevus, Blue', 'Nevus, Intradermal', 'Nevus, Spindle Cell', 'Nevus, Epithelioid and Spindle Cell', 'Rhabdoid Tumor', 'Neuroendocrine Tumors',
'Lymphoma, B-Cell, Marginal Zone', 'Carcinoma, Lewis Lung', 'Prostatic Intraepithelial Neoplasia', 'Optic Nerve Glioma', 'Lymphoma, Mantle-Cell',
'Hemangioma, Cavernous, Central Nervous System', 'Central Nervous System Venous Angioma', 'Carcinoma, Pancreatic Ductal', 'Sarcoma, Myeloid', 'Denys-Drash Syndrome',
'Gestational Trophoblastic Disease', 'Choriocarcinoma, Non-gestational', 'Mastocytosis, Cutaneous', 'Mastocytosis, Systemic', 'Mastocytoma', 'Endometrial Stromal Tumors',
'Glomus Tympanicum Tumor', 'Carcinoma, Ductal', 'Gastrointestinal Stromal Tumors', 'Myofibroma', 'Acanthoma', 'Mongolian Spot', 'Growth Hormone-Secreting Pituitary Adenoma',
'ACTH-Secreting Pituitary Adenoma', 'Odontogenic Tumor, Squamous', 'Histiocytoma', 'Histiocytoma, Malignant Fibrous', 'Nevus, Sebaceous of Jadassohn', 'Leukemia, Large Granular Lymphocytic', 'Precursor Cell Lymphoblastic Leukemia-Lymphoma', 'Precursor T-Cell Lymphoblastic Leukemia-Lymphoma',
'Neoplasms, Plasma Cell', 'Solitary Fibrous Tumor, Pleural', 'Solitary Fibrous Tumors', 'Lymphoma, Extranodal NK-T-Cell', 'Leukemia, Prolymphocytic, B-Cell', 'Leukemia, Myelomonocytic, Juvenile', 'Leukemia, Myeloid, Chronic, Atypical, BCR-ABL Negative', 'Lymphoma, Primary Cutaneous Anaplastic Large Cell', 'Lymphoma, Primary Effusion', 'Mastocytoma, Skin', 'Dendritic Cell Sarcoma, Interdigitating', 'Dendritic Cell Sarcoma, Follicular', 'Histiocytic Sarcoma', 'Langerhans Cell Sarcoma', 'Perivascular Epithelioid Cell Neoplasms', 'Adenomyoepithelioma', 'Nevus, Halo', 'Pagetoid Reticulosis', 'Carney Complex', 'Eccrine Porocarcinoma', 'Poroma', 'Desmoplastic Small Round Cell Tumor', 'Enteropathy-Associated T-Cell Lymphoma', 'Composite Lymphoma', 'Kasabach-Merritt Syndrome', 'Cystadenofibroma', 'Buschke-Lowenstein Tumor', 'Lipoblastoma', 'Intraocular Lymphoma', 'Adenocarcinoma in Situ', 'Thyroid Carcinoma, Anaplastic'],
'Neoplastic Processes': ['Oncogene Addiction', 'Extranodal Extension', 'Warburg Effect, Oncologic',
'Anaplasia', 'Cell Transformation, Neoplastic', 'Cell Transformation, Viral', 'Cocarcinogenesis', 'Lymphatic Metastasis', 'Neoplastic Cells, Circulating', 'Neoplasm Invasiveness', 'Neoplasm Metastasis', 'Neoplasm Recurrence, Local', 'Neoplasm Regression, Spontaneous', 'Neoplasm Seeding', 'Neoplasms, Unknown Primary', 'Neoplastic Processes', 'Leukemic Infiltration', 'Neoplasm, Residual', 'Neoplasm Micrometastasis', 'Carcinogenesis'],
'Precancerous Conditions': ['Smoldering Multiple Myeloma', 'Barrett Esophagus', 'Uterine Cervical Dysplasia', 'Erythroplasia', 'Leukoplakia', 'Precancerous Conditions', 'Preleukemia', 'Xeroderma Pigmentosum', 'Keratosis, Actinic', 'Aberrant Crypt Foci', 'Atypical Squamous Cells of the Cervix', 'Squamous Intraepithelial Lesions of the Cervix'],
'Paraneoplastic Syndromes': ['ACTH Syndrome, Ectopic', 'Paraneoplastic Syndromes', 'Zollinger-Ellison Syndrome'],
'Cysts': ['Basal Cell Nevus Syndrome', 'Bone Cysts', 'Branchioma', 'Bronchogenic Cyst', 'Cysts', 'Dentigerous Cyst', 'Dermoid Cyst', 'Epidermal Cyst', 'Esophageal Cyst', 'Follicular Cyst', 'Jaw Cysts', 'Lymphocele', 'Mediastinal Cyst', 'Mesenteric Cyst', 'Mucocele', 'Nonodontogenic Cysts', 'Odontogenic Cysts', 'Ovarian Cysts', 'Pancreatic Cyst', 'Pancreatic Pseudocyst', 'Parovarian Cyst', 'Periodontal Cyst', 'Pilonidal Sinus', 'Polycystic Ovary Syndrome', 'Popliteal Cyst', 'Radicular Cyst', 'Ranula', 'Synovial Cyst', 'Thyroglossal Cyst', 'Urachal Cyst', 'Choledochal Cyst', 'Arachnoid Cysts', 'Chalazion', 'Bone Cysts, Aneurysmal', 'Odontogenic Cyst, Calcifying', 'Ganglion Cysts', 'Breast Cyst', 'Tarlov Cysts', 'Colloid Cysts'],
'Neoplasms, Experimental': ['Carcinoma, Brown-Pearce', 'Neoplasms, Experimental'],
'Hamartoma': ['Hamartoma', 'Hamartoma Syndrome, Multiple', 'Tuberous Sclerosis', 'Proteus Syndrome', 'Pallister-Hall Syndrome'],
'Neoplasms, Hormone-Dependent': ['Neoplasms, Hormone-Dependent'],
'Neoplasms, Multiple Primary': ['Neoplasms, Multiple Primary'],
'Neoplasms, Radiation-Induced': ['Neoplasms, Radiation-Induced'],
'Neoplastic Syndromes, Hereditary': ['Neoplastic Syndromes, Hereditary', 'Peutz-Jeghers Syndrome', 'Li-Fraumeni Syndrome', 'Lynch Syndrome II', 'Birt-Hogg-Dube Syndrome'],
'Pregnancy Complications, Neoplastic': ['Pregnancy Complications, Neoplastic'],
'Neoplasms, Second Primary': ['Neoplasms, Second Primary'],
'Neoplasms, Post-Traumatic': ['Neoplasms, Post-Traumatic']}

######################################

def study_mesh(study):
    #recuperer tous les mesh terms cites
    mesh = []
    ancestror = []
    if study.get("derivedSection") is not None and study["derivedSection"].get("conditionBrowseModule") is not None:
        if study["derivedSection"]["conditionBrowseModule"].get("meshes") is not None:
            mesh = [i["term"] for i in study["derivedSection"]["conditionBrowseModule"]["meshes"]]
        if study["derivedSection"]["conditionBrowseModule"].get("ancestors") is not None:
            ancestror = [i["term"] for i in study["derivedSection"]["conditionBrowseModule"]["ancestors"]]
    return mesh + ancestror

######################################

def extract_year(date_str):
    #extrait uniquement l'annee d'une date sous differents formats
    match = re.search(r'\d{4}', str(date_str))  #cherche une annee a 4 chiffres
    return int(match.group()) if match else None


def parse_date(date_str):
    try:
        # Si la date est complète (YYYY-MM-DD)
        return pd.to_datetime(date_str, format="%Y-%m-%d", errors='coerce')
    except:
        # Si la date est incomplète (YYYY-MM), on ajoute le premier jour du mois
        try:
            return pd.to_datetime(date_str + "-01", format="%Y-%m-%d", errors='coerce')
        except:
            return None

###########################################################################################################################################
#charger les packages/fonctions
import pandas as pd
import re 
import requests
import dash
import datetime as dt
from fonctions import mesh_dict, study_mesh, extract_year, parse_date
###########################################################################################################################################

##EXTRACTION API

#url de l'API
base_url = "https://clinicaltrials.gov/api/v2/studies"

#parametres de la requete
params = {
    "query.cond": "neoplasm* OR cancer*",
    "query.term": "France",
    "pageSize": 1000,  #maximum etudes par page
}
total_studies = 0  #compteur d'études

#listes/dictionnaire pour stocker les donnees
liste_mesh_df = []
liste_trials_df = []
liste_loc_df = []
dico_mesh_df = {"nctid": [], "neoplasm_category": [], "neoplasm": []}

#boucle pour recuperer toutes les pages
while True:
    print("Recuperation des donnees... \netudes collectees: {}".format(total_studies)) #pour voir a quel endroit ca ne fonctionne plus
    response = requests.get(base_url, params=params)

    #si la requete a reussi
    if response.status_code == 200:
        data = response.json()  
        studies = data.get('studies', []) 

        #ajouter les etudes recuperees aux listes
        for study in studies:
            #pour trials dataframe
            nctid = study.get('protocolSection', {}).get('identificationModule', {}).get('nctId')
            condition = '\n'.join(study.get('protocolSection', {}).get('conditionsModule', {}).get('conditions'))
            startDate = study.get('protocolSection', {}).get('statusModule', {}).get('startDateStruct', {}).get('date')
            endDate = study.get("protocolSection", {}).get("statusModule", {}).get("primaryCompletionDateStruct", {}).get("date")
            drug_FDA = study.get('protocolSection', {}).get('oversightModule', {}).get('isFdaRegulatedDrug')
            device_FDA = study.get('protocolSection', {}).get('oversightModule', {}).get('isFdaRegulatedDevice')
            phase = ', '.join(study.get('protocolSection', {}).get('designModule', {}).get('phases', []))
            status = study.get('protocolSection', {}).get('statusModule', {}).get('overallStatus')
            results = study.get('hasResults')
            title = study.get("protocolSection", {}).get("identificationModule", {}).get("briefTitle")
            organization = study.get("protocolSection", {}).get("identificationModule", {}).get("organization", {}).get("fullName")
            last_update = study.get("protocolSection", {}).get("statusModule", {}).get("lastUpdateSubmitDate")
            description = study.get("protocolSection", {}).get("descriptionModule", {}).get("briefSummary")
            study_type = study.get("protocolSection", {}).get("designModule", {}).get("studyType")
            if study.get('protocolSection', {}).get('contactsLocationsModule', {}).get('centralContacts'):
                contact = study.get('protocolSection', {}).get('contactsLocationsModule', {}).get('centralContacts')[0].get("name", "")+"\n"+study.get('protocolSection', {}).get('contactsLocationsModule', {}).get('centralContacts')[0].get("email", "")
            else:
                contact = "No information"
            liste_trials_df.append([nctid, condition, startDate, endDate, drug_FDA, device_FDA, phase, status, results, title, organization, last_update, description, study_type, contact])

            #pour mesh dataframe
            mesh_id = study_mesh(study)
            for key, values in mesh_dict.items():
                #yrouver le premier element en commun entre mesh_id et values
                common_term = next((item for item in mesh_id if item in values), None) #premier element commun
                if common_term:  
                    dico_mesh_df["nctid"].append(study.get('protocolSection', {}).get("identificationModule",{}).get("nctId"))
                    dico_mesh_df["neoplasm_category"].append(key)
                    dico_mesh_df["neoplasm"].append(common_term)  


            #pour location dataframe
            for localisation in study['protocolSection'].get('contactsLocationsModule', {}).get('locations', []):
                if localisation.get('country') == 'France':
                    nctid = study.get('protocolSection', {}).get("identificationModule", {}).get("nctId")
                    facility = localisation.get("facility")
                    city = localisation.get("city")
                    country = localisation.get("country")
                    liste_loc_df.append([nctid, facility, city, country])

        total_studies += len(studies)  #mettre a jour le compteur

        #verifier s'il y a une page suivante
        nextPageToken = data.get('nextPageToken')
        if nextPageToken:
            params['pageToken'] = nextPageToken  #passer a la page suivante
        else:
            break  #sortir de la boucle si plus de page
    else:
        print("Erreur lors de la recupération des donnees. Code: {}".format(response.status_code)) #si la requete echoue
        break

#afficher le nombre total d'etudes extraites
print("Nombre total d'etudes extraites : {}".format(total_studies))
###########################################################################################################################################

##CREATION DATAFRAME

#convertir les listes en dataframes
df_mesh = pd.DataFrame(dico_mesh_df)
df_trials = pd.DataFrame(liste_trials_df, columns=["nctid", "condition", "startDate", "endDate", "drug_FDA", "device_FDA", "phase", "status", "results", "title", "organization", "last_update", "description", "study_type", "contact"])
df_loc = pd.DataFrame(liste_loc_df, columns=["nctid", "facility", "city", "country"])
###########################################################################################################################################

##DATA MANAGEMENT

#nettoyage de startDate dans df_mesh (extraction de l'annee)
df_trials["startYear"] = df_trials["startDate"].apply(extract_year)


#nettoyage de city dans df_loc
df_loc["city"] = df_loc["city"].str.replace(r'\s*cedex\s*\d*', '', flags=re.IGNORECASE, regex=True)
df_loc["city"] = df_loc["city"].str.title()  #standardisation (Paris, Lyon...)

#nettoyage de study type dans df_trials
df_trials["study_type"] = df_trials["study_type"].str.replace("_", " ").str.title()
df_trials["status"] = df_trials["status"].str.replace("_", " ").str.title()

#calcul de la duree d'un etude dans df_trials
df_trials["startDate"] = df_trials["startDate"].apply(parse_date)
df_trials["endDate"] = df_trials["endDate"].apply(parse_date)
df_trials["duration_days"] = (df_trials["endDate"] - df_trials["startDate"]).dt.days
df_trials["duration_year"] = df_trials["duration_days"]/365.25
###########################################################################################################################################
#creation de l'application dash avec le theme Cerulean 
app = dash.Dash("oncoTrials", external_stylesheets=[dbc.themes.CERULEAN], suppress_callback_exceptions=True) 

#aggregation des dataframes pour les graph


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                html.Img(
                    src="https://about.gitlab.com/images/press/logo/png/gitlab-icon-rgb.png",
                    height="30px"
                ),
                href="https://gitlab.com/hajar.abdaoui/oncotrial_tracker",
                target="_blank"  # Ouvre le lien dans un nouvel onglet
            )
        ),
    ],
    brand="📈OncoTrial Tracker",
    color="primary",
    dark=True,
)

# tabs = html.Div(
#     [html.Br(),
#         dbc.Tabs(
#             [
#                 dbc.Tab(
#                     label="Dashboard", activeTabClassName="fw-bold"
#                 ),
#                 dbc.Tab(label="Table", activeLabelClassName="fw-bold"),
#             ]
#         ),
#     ], style={"margin-top": "-20px"}
# )

tabs = html.Div(
    [html.Br(),
        dbc.Tabs(
            id='tabs',
            children=[
                dbc.Tab(label="Dashboard", activeTabClassName="fw-bold", tab_id="tab-dashboard"),
                dbc.Tab(label="Table", activeLabelClassName="fw-bold", tab_id="tab-table"),
            ]
        ),
    ], style={"margin-top": "-20px"}
)

footer = html.Footer(
    dbc.Container([
        html.Hr(),
        html.P("© 2024 Mon Dashboard", className="text-center")
    ]),
    style={"background-color": "#f8f9fa", "padding": "10px"}
)

######################################
study_counts = df_trials.groupby('startYear').size().reset_index(name='count')

fig_year_count = px.line(
    study_counts,
    x='startYear',
    y='count',
    labels={'startYear': 'Year', 'count': 'Studies'},
    title='Studies Started Each Year',
    markers=True,  # Ajoute des points sur la ligne
    color_discrete_sequence=['#007BA7']  # Couleur principale (bleu Bootstrap)
)

fig_year_count.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',   #fond transparent
    paper_bgcolor='rgba(0,0,0,0)',  #fond transparent
    font=dict(family="Arial", size=9, color="#333"),
    title_x=0.5,  #centrage du titre
    margin=dict(l=20, r=20, t=40, b=20),
    hovermode="x unified"  #survol des points
)

fig_year_count.update_xaxes(range=[1990, 2027])

######################################
completed = df_trials[df_trials["status"]=="Completed"]#.dropna(subset=["duration_year"])

fig_box_duration = px.box(
    completed,
    y="duration_year",
    title="Duration of completed studies",
    labels={"Years"},
    color_discrete_sequence=["#007BA7"]  # Couleur principale (bleu Bootstrap)
)

fig_box_duration.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',   # fond transparent
    paper_bgcolor='rgba(0,0,0,0)',  # fond transparent
    font=dict(family="Arial", size=9, color="#333"),
    title_x=0.5,  # centrage du titre
    margin=dict(l=20, r=20, t=40, b=20),  # marges similaires au graphique linéaire
    height=450,
    width=450
)

fig_box_duration.update_yaxes(range=[0, 20], title="Duration in years")  # Plage et titre de l'axe Y
fig_box_duration.update_traces(marker=dict(color='#007BA7'))  # Garde la même couleur bleue que le graphique linéaire

######################################
drug_pourcentage = round(len(df_trials[df_trials.drug_FDA == True])*100/(len(df_trials[df_trials.drug_FDA == True]) + len(df_trials[df_trials.drug_FDA == False])),1)
device_pourcentage = round(len(df_trials[df_trials.device_FDA == True])*100/(len(df_trials[df_trials.device_FDA == True]) + len(df_trials[df_trials.device_FDA == False])),1)

cards_info = [
    {"title": "Total Trials", "content": len(df_trials)},
    {"title": "Completed Trials", "content": len(completed)},
    {"title": "FDA Regulated Drug Product", "content": "{} %".format(drug_pourcentage)},
    {"title": "FDA Regulated Device Product", "content": "{} %".format(device_pourcentage)}
]

card_layout = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H5(card["title"], className="card-title"),
                    html.H4(card["content"], className="card-text")
                ])
            ),
            width=3,  # Chaque colonne prendra 3/12 de l'espace (total 4 cases)
        ) for card in cards_info
    ],
    justify="between",  # Espace entre les colonnes
    className="mb-4"
)

######################################

categories = df_mesh['neoplasm_category'].unique()
@app.callback(
    Output('top-neoplasms-graph', 'figure'),
    Input('category-dropdown', 'value')
)
def update_graph(selected_category):
    # Filtrer le DataFrame en fonction de la catégorie sélectionnée
    df_filtered = df_mesh[df_mesh['neoplasm_category'] == selected_category]

    # Compter le nombre d'études par néoplasme
    count_df = df_filtered['neoplasm'].value_counts().reset_index()
    count_df.columns = ['neoplasm', 'count']
    count_df = count_df.sort_values(by='count', ascending=False)

    # Sélectionner les 10 néoplasmes les plus fréquents
    top_10_df = count_df.head(10)

    # Création de la figure harmonisée
    fig = px.bar(
        top_10_df,
        x='neoplasm',
        y='count',
        labels={'neoplasm': 'Classe de Néoplasme', 'count': "Nombre d'Études"},
        title=f"📊 Les 10 Néoplasmes les Plus Étudiés ({selected_category})",
        color_discrete_sequence=["#1f77b4"]  # Même bleu que le boxplot
    )

    # Mise en forme harmonisée
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',    # Fond transparent
        paper_bgcolor='rgba(0,0,0,0)',   # Fond transparent
        font=dict(family="Arial", size=14, color="#333"),  # Police uniforme
        title_x=0.5,                     # Titre centré
        margin=dict(l=40, r=40, t=60, b=120),
        height=550,
        hovermode="x unified"            # Effet de survol unifié
    )

    fig.update_xaxes(tickangle=-45)     # Inclinaison des étiquettes X
    fig.update_yaxes(showgrid=True, gridcolor='lightgrey')  # Grille légère

    return fig
######################################

df=df_trials[df_trials.results==True]
last_results = df[["nctid", "title", "organization", "description", "last_update"]].sort_values(by='last_update', ascending=False).head(5)

study_cards = [
    dbc.Card(
        dbc.CardBody([
            html.A(study["title"], href="https://clinicaltrials.gov/ct2/show/{}".format(study["nctid"]), target="_blank"),
            html.H6(study['organization'], className="card-subtitle mb-2 text-muted"),
            html.P(study["description"], className="card-text", style={"text-align": "justify"}),
            html.Footer(f"Last Update: {study['last_update']}", className="text-end text-secondary")
        ]),
        className="mb-3 shadow-sm p-2 bg-light rounded"
    )
    for _, study in last_results.iterrows()
]
######################################

content = dbc.Container(
    [
        # Section des cartes principales
        card_layout,

        # Section combinée : Encadré + Graphique linéaire + Boxplot
        dbc.Row([
            # Colonne principale (Encadré + Graphique linéaire)
            dbc.Col([
                # Encadré d'information
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Study Trends Over the Years", className="fw-bold text-primary"),
                        html.P(
                            "This graph shows the annual distribution of studies, providing insights into research trends over time.",
                            style={"text-align": "justify"}
                        )
                    ]),
                    className="shadow-sm p-3 mb-3 bg-light rounded"
                ),

                # Graphique linéaire
                dbc.Card(
                    dbc.CardBody(
                        dbc.Spinner(
                            dcc.Graph(id='study-year-graph', figure=fig_year_count,
                                      style={"width": "100%", "height": "300px", "margin": "0"}),
                            color="primary"
                        )
                    ),
                    className="shadow-sm p-3 mb-4 bg-white rounded",
                    style={"width": "100%"}
                )
            ], width=8),

            # Boxplot aligné à droite
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        dbc.Spinner(
                            dcc.Graph(id='study-duration-graph', figure=fig_box_duration,
                                      style={"width": "100%", "height": "459px", "margin": "0"}),
                            color="primary"
                        )
                    ),
                    className="shadow-sm p-3 mb-4 bg-white rounded",
                    style={"width": "100%"}
                ),
                width=4
            )
        ], justify="between"),

        # Section Dropdown + Texte descriptif
        dbc.Row([
            # Dropdown + Graphique des néoplasmes
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        dcc.Dropdown(
                            id='category-dropdown',
                            options=[{'label': cat, 'value': cat} for cat in categories],
                            value='Neoplasms by Site',
                            clearable=False
                        ),
                        dbc.Spinner(
                            dcc.Graph(id='top-neoplasms-graph'),
                            color="primary"
                        )
                    ]),
                    className="shadow-sm p-3 mb-4 bg-white rounded"
                ),
                width=6
            ),

            # Deux encadrés de texte descriptif
            dbc.Col([
                # Premier encadré
                dbc.Card(
                    dbc.CardBody([
                        html.P(
                            '''MeSH (Medical Subject Headings) is a controlled vocabulary 
developed by the National Library of Medicine (NLM) to index, organize, and search biomedical information 
in databases like PubMed and ClinicalTrials.gov. It follows a hierarchical structure, allowing terms to be 
classified from broad categories to more specific subcategories. For example, Neoplasms is a primary category, 
which branches into subcategories like Neoplasms by Site, Neoplasms by Histologic Type, and Cysts. 
This structure helps standardize medical terminology, improve the accuracy of search queries, 
and link related research topics.''',
                            className="text-danger",
                            style={"text-align": "justify"}
                        )
                    ]),
                    className="shadow-sm p-3 mb-3 bg-white rounded",
                    style={"height": "250px", "overflowY": "auto"}  # Texte défilable
                ),

                # Deuxième encadré
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Latest 5 Studies", className="fw-bold text-center mb-3 text-success"),
                        html.Div(study_cards, style={"height": "400px", "overflowY": "auto"})  # Scrollable
                    ]),
                    className="shadow-sm p-3 bg-white rounded",
                    style={"height": "385px", "overflowY": "auto"}  # Texte défilable
                )
            ], width=6)
        ])
    ],
    fluid=True,
    className="mt-4"
)

######################################

df_loc_grouped = df_loc.groupby("nctid").agg({
    "facility": lambda x: "\n".join(sorted(set(x.dropna()))),
    "city": lambda x: "\n".join(sorted(set(x.dropna()))),
    "country": "first"
}).reset_index()

# Fusion des DataFrames
df_combined = pd.merge(df_trials, df_loc_grouped, on="nctid", how="inner")[[
    "title", "organization", "condition", "study_type", "status", "city", "contact"
]]

# Renommer les colonnes pour plus de clarté
df_combined.rename(columns={
    "title": "Title",
    "organization": "Organization",
    "condition": "Condition",
    "study_type": "Type",
    "city": "Location",
    "status": "Status",
    "contact": "Contact"
}, inplace=True)
######################################

content2 = dbc.Container([
    html.H1("Tableau des Essais Cliniques", className="text-center my-4 fw-bold text-primary"),

    dbc.Card(
        dbc.CardBody([
            dash_table.DataTable(
                id='table',
                columns=[
                    {"name": col, "id": col, "deletable": False} 
                    for col in df_combined.columns
                ],
                data=df_combined.to_dict('records'),
                page_size=10,
                filter_action="native",  # Activation du filtrage natif
                sort_action="native",    # Activation du tri natif
                sort_mode="multi",       # Tri sur plusieurs colonnes
                column_selectable='single',  # Activation de la sélection de colonnes
                style_table={'overflowX': 'auto'},
                style_cell={
                    'whiteSpace': 'pre-line',  # Support du saut de ligne '\n'
                    'textAlign': 'left',
                    'padding': '10px',
                    'fontFamily': 'Arial'
                },
                style_header={
                    'backgroundColor': '#007BA7',
                    'color': 'white',
                    'fontWeight': 'bold',
                    'textAlign': 'center'
                },
                style_data={
                    'backgroundColor': 'white',
                    'color': 'black'
                },
                style_data_conditional=[
                    {  # Effet zébré pour les lignes impaires
                        'if': {'row_index': 'odd'},
                        'backgroundColor': '#F9F9F9'
                    }
                ]
            )
        ]),
        className="shadow-sm p-4 bg-white rounded"
    )
], fluid=True)


######################################
# app.layout = html.Div([
#     dcc.Location(id="url"),
#     navbar, tabs, content, footer
# ])
@app.callback(
    Output('tab-content', 'children'),
    Input('tabs', 'active_tab')
)
def display_tab_content(active_tab):
    if active_tab == 'tab-dashboard':
        return content  # Affiche le contenu du dashboard pour l'onglet "Dashboard"
    elif active_tab == 'tab-table':
        return content2  # Affiche content2 pour l'onglet "Table"
    return content  # Par défaut, afficher le contenu du dashboard

app.layout = html.Div([
    dcc.Location(id="url"),
    navbar, tabs, html.Div(id='tab-content'), footer
])

if __name__ == '__main__':
    app.run_server(debug=True)

