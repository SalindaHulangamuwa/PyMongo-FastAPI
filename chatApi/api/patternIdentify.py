from fastapi import HTTPException
# import spacy
# from spacy.matcher import Matcher
import re

async def find_placeholders(text: str):
    if not text:
        raise HTTPException(status_code=400, detail="Text input is required.")

    regex_pattern = r"([A-Z]+)_([A-Za-z0-9+/=]+)(?:'s)?"
    
    direct_matches = []
    prefixes = []
    ids = []
    full_details = []
    
    if text:
        matches = re.finditer(regex_pattern, text)
        for match in matches:
            full_match = match.group(0)  
            prefix = match.group(1)      
            id_part = match.group(2)    
            
            direct_matches.append(full_match)
            prefixes.append(prefix)
            ids.append(f"{prefix}_{id_part}")
            
            full_details.append({
                "full_match": full_match,
                "type": prefix,
                "id": f"{prefix}_{id_part}",
                "position": match.span()  
            })
    
    # nlp = spacy.load("en_core_web_lg")
    # matcher = Matcher(nlp.vocab)

    # pattern = [
    #     {"TEXT": {"REGEX": r"^[A-Z]+_[A-Za-z0-9+/=]+('s)?$"}}
    # ]
    # matcher.add("API_PLACEHOLDER_PATTERN", [pattern])
    
    # doc = nlp(text)
    # spacy_matches = matcher(doc)
    # spacy_results = [doc[start:end].text for match_id, start, end in spacy_matches]
    
    # all_matches = list(set(direct_matches + spacy_results))
    
    return {
        "matches": direct_matches,
        "prefixes": list(set(prefixes)), 
        "ids": list(set(ids)),           
        "details": full_details           
    }