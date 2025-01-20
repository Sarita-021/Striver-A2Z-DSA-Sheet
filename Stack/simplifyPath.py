'''You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. 
Your task is to transform this absolute path into its simplified canonical path.'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        st = []

        for comp in components:
            if comp == "" or comp == ".":
                continue
            
            if comp == "..":
                if st:
                    st.pop()
            else:
                st.append(comp)
        
        return "/" + "/".join(st)