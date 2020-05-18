p: Project = input;
repoRatio: output collection[string] of float;
pfiles: output collection[string] of string;

exists(plangs: int; match(`^python$`, lowercase(p.programming_languages[plangs]))) {
    foreach (i: int; def(p.code_repositories[i])) {
        if (p.code_repositories[i].kind == RepositoryKind.GIT) {
            snaps: array of ChangedFile;
            snaps = getsnapshot(p.code_repositories[i], "OTHER");
            if (len(snaps) > 0) {
                ratio: float;
                numPy: float;
                foreach (cf: int; def(snaps[cf])) {
                    file_name: string;
                    file_name = snaps[cf].name;
                    # if file ends with .py then add to results
                    if (match("\\.py$", file_name)) {
                        pfiles[p.code_repositories[i].url] << file_name;
                        numPy = numPy + 1.0;
                    }
                }
                ratio = (numPy / len(snaps)) * 100;
                repoRatio[p.code_repositories[i].url] << ratio;
            }
        }
    }
}